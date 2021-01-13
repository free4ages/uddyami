from django.contrib import admin

from .models import CropBudget

# Register your models here.

class CropBudgetAdmin(admin.ModelAdmin):
    list_display = ('crop_name',)
    prepopulated_fields={'crop_slug':('crop_name',)}


admin.site.register(CropBudget,CropBudgetAdmin)


