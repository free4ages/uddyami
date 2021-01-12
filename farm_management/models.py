from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings
from model_utils.managers import InheritanceManager
from django.core.exceptions import ValidationError
import re

# Create your models here.
class FarmManager(models.Manager):

    def new_farm(self, farm):
        new_farm = self.create(farm=re.sub('\s+', '-', farm)
                                   .lower())

        new_farm.save()
        return new_farm

def validate_image(image):
    file_size = image.file.size
    limit_kb = 25
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" %limit_kb)

class Farm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,verbose_name=_("User"), on_delete=models.CASCADE)
    farm = models.CharField(
        verbose_name=_("Plot"),
        max_length=50, blank=True, null=True)

    farm_owner = models.CharField(
        verbose_name=_("Farmer"),
        max_length=50, blank=True, null=True)
    address = models.CharField(verbose_name=_("Address"),max_length=100,blank=True)

    notes = models.TextField(blank=True, null=True)

    image_1 = models.ImageField(upload_to='media/%Y/%m/%d ',
                              blank=True,
                              null=True,
                              verbose_name=_("Plot Image"),
                              validators=[validate_image])

    image_2 = models.ImageField(upload_to='media/%Y/%m/%d ',
                              blank=True,
                              null=True,
                              verbose_name=_("Plot Image"),
                              validators=[validate_image])

    date_added = models.DateTimeField(auto_now_add=True)

    objects = FarmManager()

    class Meta:
        verbose_name = _("Plot")
        verbose_name_plural = _("Plots")
        permissions = (("monitor_data", _("Monitor Data")),)


    def __str__(self):
        return self.farm

class Location(models.Model):

    location = models.CharField(
        verbose_name=_("Location"),
        max_length=50, blank=True, null=True)

    image = models.ImageField(upload_to='media/%Y/%m/%d ',
                              blank=True,
                              null=True,
                              verbose_name=_("Location Image"),
                              validators=[validate_image] )

    notes = models.TextField(blank=True, null=True)

    farm = models.ForeignKey(
        Farm, null=True, blank=True,
        verbose_name=_("Plot"), on_delete=models.CASCADE)

    objects = FarmManager()

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __str__(self):
        return self.location + "-" + str(self.farm.farm) + "-" +str(self.farm.farm_owner)

class Sensor_Data(models.Model):

    location = models.ForeignKey(
        Location, null=True, blank=True,
        verbose_name=_("Location"), on_delete=models.CASCADE)

    date_added = models.DateTimeField(auto_now_add=True)

    #Sensor Readings
    pH = models.CharField(max_length=3,default="",blank=True,help_text='pH value(0-14) ')
    Moisture = models.CharField(max_length=6,default="",blank=True,help_text='Moisture Value ')
    Humidity = models.CharField(max_length=4,default="",blank=True,help_text='Humidity Value ')
    Temperature = models.CharField(max_length=4,default="",blank=True,help_text='Temperature in degree C ')
    Light = models.CharField(max_length=4,default="",blank=True,help_text='Light value ')
    Co2_level = models.CharField(max_length=4,default="",blank=True,help_text='Carbon Dioxide(Co2) value ')
    Wind = models.CharField(max_length=4,default="",blank=True,help_text='Wind data ')
    SunTracking = models.CharField(max_length=8,default="",blank=True,help_text='Sun Tracking ')

    objects = InheritanceManager()

    class Meta:
        verbose_name = _("Sensor_Da")
        verbose_name_plural = _("Sensor_Das")

