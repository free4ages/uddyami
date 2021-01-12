from django.db import models
import re
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

def validate_image(image):
    file_size = image.file.size
    limit_kb = 25
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" %limit_kb)

class SaleItem(models.Model):
    product_name = models.CharField(
        verbose_name = ("Product"),
        max_length = 200)
    description= models.TextField(blank=True,default="")
    company_name = models.CharField(
        verbose_name = ("Company Name"),
        max_length = 200,blank=True,default="")
    seller_name = models.CharField(
        verbose_name = ("Seller Name"),
        max_length = 50)
    email = models.EmailField(max_length = 254,blank=True,default="")
    mobile = models.CharField(max_length=10,default="",help_text='Mobile Number(10 digits) ')
    whatsapp = models.CharField(max_length=10,blank=True,default="",help_text='WhatsApp Number(10 digits) ')
    address = models.TextField(blank=True,default="")
    city = models.CharField(max_length=50,blank=True,default="")
    state = models.CharField(max_length=50,blank=True,default="Bihar")
    date_added = models.TimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    sticky = models.BooleanField(default=False)
    whatsapp_active = models.BooleanField(default=True)
    product_image = models.ImageField(upload_to='media/%Y/%m/%d ',
                              blank=True,
                              null=True,
                              verbose_name=_("Product Image"),validators=[validate_image]
                            )



