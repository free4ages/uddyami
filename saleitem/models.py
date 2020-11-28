from django.db import models
import re
from django.utils.translation import ugettext_lazy as _


class SaleItem(models.Model):
    product_name = models.CharField(
        verbose_name = ("Product"),
        max_length = 200)
    company_name = models.CharField(
        verbose_name = ("Company Name"),
        max_length = 200,blank=True,default="")
    seller_name = models.CharField(
        verbose_name = ("Seller Name"),
        max_length = 50)
    email = models.EmailField(max_length = 254,blank=True,default="")
    mobile = models.CharField(max_length=15,blank=True,default="")
    address = models.CharField(max_length=500,blank=True,default="")
    city = models.CharField(max_length=50,blank=True,default="")
    state = models.CharField(max_length=50,blank=True,default="Bihar")
    description= models.TextField(blank=True,default="")
    date_added = models.TimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    sticky = models.BooleanField(default=False)
    whatsapp_active = models.BooleanField(default=True)
    product_image = models.ImageField(upload_to='media/%Y/%m/%d ',
                              blank=True,
                              null=True,
                              verbose_name=_("Product Image"),
                            )

        

