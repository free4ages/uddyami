from django.contrib import admin
from .models import SaleItem
# Register your models here.


class SaleItemAdmin(admin.ModelAdmin):
    search_fields = ('product_name','seller_name','mobile',)
    list_display = ('product_name','seller_name','mobile','city',)
    list_filter = ('city',)


admin.site.register(SaleItem, SaleItemAdmin)
