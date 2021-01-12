from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.

class CropPlan(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,verbose_name=_("User"), on_delete=models.CASCADE)
    plan = models.CharField(max_length=20,help_text = "Plan Identifier/Name")

    bigha = models.IntegerField(default=0, help_text = "Land Area in Bigha")
    kattha = models.IntegerField(default=0, help_text = "Kattha")

    KATTHA_TO_SQFEET = (
        (720, 'Choti'),
        (1020, 'Badi'), )
    ACRE_TO_SQFEET = 43560

    katthaToSqFeet = models.IntegerField(default=1020, choices=KATTHA_TO_SQFEET,help_text = "Kattha To Sq. Feet")
    area = models.IntegerField(default = 0, help_text = "Area in Acre")

    class Season(models.TextChoices):
        SPRING = 'FR', _('Spring')
        SUMMER = 'SO', _('Summer')
        AUTUMN = 'JR', _('Autumn')
        WINTER = 'SR', _('Winter')


    season =  models.CharField(max_length=2,choices=Season.choices,default=Season.SUMMER,)

    class Crop(models.TextChoices):
        KARELA = 'BIGO', _('Bitter Gourd')
        TOMATO = 'TOMA', _('Tomato')
        WATERMELON = 'WATM', _('Water Melon')
        MIRCHI = 'MIRC', _('Green Chilli')
        KHIRA = 'KHIR', _('Cucumber')

    crop =  models.CharField(max_length=4,choices=Crop.choices,default=Crop.MIRCHI,)

    class Plantation(models.TextChoices):
        SEED = 'SE', _('Seed')
        SEEDLING = 'SI', _('Seedling')

    seeding = models.CharField(max_length=2,choices=Plantation.choices,default=Plantation.SEEDLING,)
    seeding_date = models.DateField(help_text = "Date of seeding")
    fertigation_plan = models.TextField(help_text = "Fertigation Plan")
    plant_protection_plan = models.TextField(help_text = "Plant Protection Plan")
    weeding_plan = models.TextField(help_text = "Weeding Plan")
    labour_planning = models.TextField(help_text = "Labour Management Plan")
    class Meta:
        verbose_name = _("Crop Plan")
        verbose_name_plural = _("Crop Plans")

    def __str__(self):
        return self.plan
