from django.db import models
import re
from django.utils.translation import ugettext_lazy as _
from model_utils.managers import InheritanceManager

# Create your models here.
class CategoryManager(models.Manager):

    def new_category(self, category):
        new_category = self.create(category=re.sub('\s+', '-', category)
                                   .lower())

        new_category.save()
        return new_category

class Category(models.Model):

    category = models.CharField(
        verbose_name=_("Category"),
        max_length=200, blank=True,
        unique=True, null=True)

    objects = CategoryManager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category

class SubCategory(models.Model):

    sub_category = models.CharField(
        verbose_name=_("Sub-Category"),
        max_length=200, blank=True, null=True)

    category = models.ForeignKey(
        Category, null=True, blank=True,
        verbose_name=_("Category"), on_delete=models.CASCADE)

    objects = CategoryManager()

    class Meta:
        verbose_name = _("Sub-Category")
        verbose_name_plural = _("Sub-Categories")

    def __str__(self):
        return self.sub_category


class Product(models.Model):
    """
    Base class for all product types.
    Shared properties placed here.
    """
    title = models.CharField(('Product'),max_length=50, default = 'Food')
    category = models.ForeignKey(Category,
                                 verbose_name=_("Category"),
                                 blank=True,
                                 null=True,
                                 on_delete=models.CASCADE)

    sub_category = models.ForeignKey(SubCategory,
                                     verbose_name=_("Sub-Category"),
                                     blank=True,
                                     null=True,
                                     on_delete=models.CASCADE)


    objects = InheritanceManager()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ['category']

    def __str__(self):
        return self.title

