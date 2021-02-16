from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.exceptions import ValidationError

def validate_image(image):
    file_size = image.file.size
    limit_kb = 25
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" %limit_kb)

# Create your models here.

class CropBudget(models.Model):
    """
    Attributes associated with crop for cost and profit calculation
    """
    crop_name = models.CharField(max_length=30,help_text="Name of Crop")
    crop_slug = models.SlugField(max_length=30)
    crop_image = models.ImageField(upload_to='%Y/%m/%d',blank=True,null=True,verbose_name=_("Crop Image"),validators=[validate_image])
    sticky = models.BooleanField(default=False)

    #Basic Checking
    seed_check = models.BooleanField(default=True)
    seedling_check = models.BooleanField(default=False)
    prod_per_plant_av = models.BooleanField(default=True)
    mulch_check = models.BooleanField(default=True)
    alan_check = models.BooleanField(default=True)
    stake_check = models.BooleanField(default=True)
    crop_cover_check = models.BooleanField(default=True)
    gobar_check = models.BooleanField(default=True)
    vermi_check = models.BooleanField(default=True)
    #basal dose
    fertiliz_bas_check = models.BooleanField(default=True)
    #water soluble
    fertiliz_ws_check = models.BooleanField(default=True)
    marketing_check = models.BooleanField(default=True)
    management_check = models.BooleanField(default=True)
    lease_check = models.BooleanField(default=True)
    miscell_check = models.BooleanField(default=True)

    #Sales and production data
    num_plants_acre = models.IntegerField(default=0)
    prod_per_plant_min = models.FloatField(default=0,help_text="in Kgs")
    prod_per_plant_max = models.FloatField(default=0,help_text="in Kgs")

    prod_per_acre_min = models.FloatField(default=0,help_text="in Kgs")
    prod_per_acre_max = models.FloatField(default=0,help_text="in Kgs")


    sell_price_min = models.FloatField(default=0, help_text="Rs. per Kg")
    sell_price_max = models.FloatField(default=0, help_text="Rs. per Kg")

    crop_duration = models.IntegerField(default=6,help_text="Duration in months")

    # Seed Cost Per Acre
    seed_cost = models.FloatField(default=0, help_text="Seed Cost per Acre")
    per_plant_cost = models.FloatField(default=0, help_text="Rs. per plant")

    vermi_compost_cost = models.IntegerField(default=0, help_text="Cost per Acre")
    plantation_cost = models.IntegerField(default=0, help_text="Cost per Acre")
    fertilizer_bas_cost = models.IntegerField(default=0, help_text="Basal Dose Fertilizer Cost per Acre")
    fertilizer_ws_cost = models.IntegerField(default=0, help_text="Water Soluble Fertilizer Cost per Acre")
    pesticide_cost = models.IntegerField(default=0,help_text="Cost per Acre")
    irrigation_cost = models.IntegerField(default=0,help_text="Cost per Acre")

    #Additional Cost
    marketing_and_harvesting_cost = models.IntegerField(default=0, help_text="Cost for Crop Cycle")

    #Fixed Cost
    gobar_cost = models.IntegerField(default=0,help_text="Yearly Cost")
    ploughing_bed_cost = models.IntegerField(default=0, help_text="Yearly Cost")

    #Mulching Cost
    mulch_cost = models.IntegerField(default=0, help_text="Yearly Cost")
    mulch_labour_cost = models.IntegerField(default=0, help_text="Yearly Cost")
    weeding_cost = models.IntegerField(default=0, help_text="Yearly Cost")

    alan_cost = models.IntegerField(default=0, help_text="Yearly Cost")
    wire_stake = models.IntegerField(default=0, help_text="Yearly Cost")
    wire_thin_tant = models.IntegerField(default=0, help_text="Yearly Cost")
    stake_labour_cost = models.IntegerField(default=0, help_text="Yearly Cost")

    # Crop Cover Cost
    crop_cover = models.IntegerField(default=0, help_text="Yearly Cost for Crop Cover")
    wire_cost = models.IntegerField(default=0, help_text="Cost for Crop Cover Structure Wire")
    wire_recov_duration = models.IntegerField(default=48,help_text="Crop Cover Structure Wire Recovery period In Months")
    labour_crop_cover = models.IntegerField(default=0, help_text="Yearly Cost")


    land_lease_cost = models.IntegerField(default=0,help_text="Land lease per acre cost in INR per year")

    plant_guarding_maintenance_cost = models.IntegerField(default=0, help_text="Monthly Cost in INR")

    management_cost = models.IntegerField(default=0, help_text="Monthly Cost in INR")

    miscell_cost = models.IntegerField(default=0, help_text="Cost in INR for crop cycle")



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
