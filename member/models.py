from django.db import models
from django.utils.translation import ugettext_lazy as _
from product.models import Product
from model_utils.managers import InheritanceManager
from django.core.exceptions import ValidationError
import re

# Create your models here.
class StateManager(models.Manager):

    def new_state(self, state):
        new_state = self.create(state=re.sub('\s+', '-', state)
                                   .lower())

        new_state.save()
        return new_state

class State(models.Model):

    state = models.CharField(
        verbose_name=_("State"),
        max_length=50, blank=True,
        unique=True, null=True)

    objects = StateManager()

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        return self.state

class District(models.Model):

    district = models.CharField(
        verbose_name=_("District"),
        max_length=50, blank=True, null=True)

    state = models.ForeignKey(
        State, null=True, blank=True,
        verbose_name=_("State"), on_delete=models.CASCADE)

    objects = StateManager()

    class Meta:
        verbose_name = _("District")
        verbose_name_plural = _("Districts")

    def __str__(self):
        return self.district

def validate_image(image):
    file_size = image.file.size
    limit_kb = 25
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" %limit_kb)


class Member(models.Model):
    name = models.CharField(('Name'), max_length=50)
    enterprise_name = models.CharField(('Enterprise Name'), max_length=70,null=True, blank=True)
    figure = models.ImageField(upload_to='media/%Y/%m/%d ',
                              blank=True,
                              null=True,
                              verbose_name=_("Member Image"),
                              validators=[validate_image] )

    mobile_number = models.CharField(('Mobile Number'), max_length=10, unique=True)
    whatsapp_number = models.CharField(('WhatsApp Number'), max_length=10, blank=True,)
    email = models.EmailField(null=True, blank=True)

    address = models.CharField(('Address'),max_length=70,blank=True)
    pin_code = models.CharField(('Pin Code'), max_length=6, blank=True)
    district = models.ForeignKey(District,
                                     verbose_name=_("District"),
                                     blank=True,
                                     null=True,
                                     on_delete=models.CASCADE)
    state = models.ForeignKey(State,
                                 verbose_name=_("State"),
                                 blank=True,
                                 null=True,
                                 on_delete=models.CASCADE)


    comments = models.TextField(blank=True, null=True)


    products = models.ManyToManyField(Product,
                                  verbose_name=_("Product"),
                                  blank=True)

    active = models.BooleanField(default=True)
    sticky = models.BooleanField(default=False)
    whatsapp_active = models.BooleanField(default=True)
    objects = InheritanceManager()


    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Members")
        permissions = (('view_members', 'View Members'),)

    def __str__(self):
        return self.name


