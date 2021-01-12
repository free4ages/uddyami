from django.db import models
import re
from django.utils.translation import ugettext_lazy as _

def validate_image(image):
    file_size = image.file.size
    limit_kb = 20
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" %limit_kb)

# Create your models here.
class JobPost(models.Model):
    job_title = models.CharField(
        verbose_name = ("Title"),
        max_length = 200)
    salary = models.CharField(
        verbose_name = ("Salary"),
        max_length = 100)
    qualification = models.CharField(
        verbose_name = ("Qualification"),
        max_length = 200)
    work_hours = models.CharField(
        verbose_name = ("Work Hours"),
        max_length = 200)
    description= models.TextField(blank=True,default="")
    company_name = models.CharField(
        verbose_name = ("Company Name"),
        max_length = 200,blank=True,default="")
    contact_person = models.CharField(
        verbose_name = ("Contact Person"),
        max_length = 50)
    email = models.EmailField(max_length = 254,blank=True,default="")
    mobile = models.CharField(max_length=10,default="",help_text='Mobile Number(10 digits) ')
    whatsapp = models.CharField(max_length=10,blank=True,default="",help_text='WhatsApp Number(10 digits) ')
    location = models.TextField(blank=True,default="")
    city = models.CharField(max_length=50,blank=True,default="")
    state = models.CharField(max_length=50,blank=True,default="Bihar")
    date_added = models.TimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    sticky = models.BooleanField(default=False)
    whatsapp_active = models.BooleanField(default=True)
    job_image = models.ImageField(upload_to='media/%Y/%m/%d ',
                              blank=True,
                              null=True,
                              verbose_name=_("Job Image"),validators=[validate_image]
                            )
