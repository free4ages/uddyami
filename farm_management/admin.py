from django.contrib import admin
from .models import Farm, Location, Sensor_Data
from django.utils.safestring import mark_safe
from django.urls import reverse
# Register your models here.


class EditLinkToInlineObject(object):
    def edit_link(self, instance):
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk] )
        if instance.pk:
            return mark_safe(u'<a href="{u}"><b>Edit</b></a>'.format(u=url))
        else:
            return 'save and continue editing to create a link'

class LocationInline(EditLinkToInlineObject, admin.StackedInline):
    model = Location
    extra = 4
    fields = ('location', 'image','notes','farm','edit_link')
    readonly_fields = ('image','edit_link')

class Sensor_DataInline(EditLinkToInlineObject, admin.StackedInline):
    model = Sensor_Data
    extra = 5

class FarmAdmin(admin.ModelAdmin):
    search_fields = ('user', 'farm_owner')
    list_display = ('user','farm','farm_owner','address',)
    list_filter = ('user','farm_owner')
    save_on_top = True
    inlines = [LocationInline]

class LocationAdmin(admin.ModelAdmin):
    search_fields = ('farm',)
    list_display = ('location','farm',)
    list_filter = ('farm',)
    save_on_top = True
    inlines = [Sensor_DataInline]

class Sensor_DataAdmin(admin.ModelAdmin):
    search_fields = ('location',)
    list_display = ('location',)
    list_filter = ('location',)



admin.site.register(Farm, FarmAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Sensor_Data, Sensor_DataAdmin)

