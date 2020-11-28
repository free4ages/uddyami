from django.contrib import admin
from .models import Product, Category, SubCategory
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category', )


class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ('sub_category', )
    list_display = ('sub_category','category', )
    list_filter = ('sub_category','category',)

class ProductAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'sub_category',)
    list_filter = ('sub_category','category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)