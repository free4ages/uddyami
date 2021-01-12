from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.views.generic.base import TemplateView


from django import forms

from saleitem.models import SaleItem

class SaleItemForm(forms.ModelForm):
    mobile = forms.CharField(max_length=10)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    class Meta:
        model = SaleItem
        fields = ['product_name','company_name','seller_name','email','mobile','whatsapp','address','city','state','description','whatsapp_active']

class SaleItemList(ListView):
    queryset = SaleItem.objects.exclude(active = 'False').order_by('sticky','date_added')
    template_name = 'saleitem/saleitem-list.html'
    context_object_name = 'saleitems'

class SaleItemCreate(View):
    template_name = 'saleitem/saleitem-form.html'
    form_class = SaleItemForm
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/sale/success/')
        return render(request, self.template_name, {'form': form})

class SaleSuccess(TemplateView):
    template_name = 'saleitem/saleitem-success.html'

