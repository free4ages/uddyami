from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from product.models import Product
from .models import Member, State, District
# Register your models here.

class MemberAdminForm(forms.ModelForm):
    """
    below is from
    http://stackoverflow.com/questions/11657682/
    django-admin-interface-using-horizontal-filter-with-
    inline-manytomany-field
    """

    class Meta:
        model = Member
        exclude = []

    PRODUCT_QUERY = Product.objects.all().select_subclasses().order_by('category','sub_category', )

    products = forms.ModelMultipleChoiceField(queryset= PRODUCT_QUERY,
        required=False, label=_("Products"), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(MemberAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['products'].initial =\
                self.instance.products.all()

    def save(self, commit=True):
        member = super(MemberAdminForm, self).save(commit=False)
        member.save()
        member.products.set(self.cleaned_data['products'])
        self.save_m2m()
        return member

class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminForm
    search_fields = ('name','enterprise_name','mobile_number',)
    list_display = ('name','enterprise_name','mobile_number','address' )
    list_filter = ('products','district','state' )

class StateAdmin(admin.ModelAdmin):
    search_fields = ('state', )


class DistrictAdmin(admin.ModelAdmin):
    search_fields = ('district', )
    list_display = ('district','state', )
    list_filter = ('state',)


admin.site.register(Member, MemberAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(District, DistrictAdmin)


