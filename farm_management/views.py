from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views import View
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied

from django import forms

from farm_management.models import Farm, Location, Sensor_Data

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['farm','farm_owner','address','notes','image_1','image_2']

class FarmList(ListView):
    queryset = Farm.objects.order_by('date_added')
    template_name = 'farm_management/farm-list.html'
    context_object_name = 'farms'

class FarmCreate(View):
    template_name = 'farm_management/farm-form.html'
    form_class = FarmForm

    @method_decorator(login_required)
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/farm/success/')
        return render(request, self.template_name, {'form': form})

class FarmSuccess(TemplateView):
    template_name = 'farm_management/farm-success.html'

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location','image','notes']


class LocationCreate(View):
    template_name = 'farm_management/location-form.html'
    form_class = LocationForm
    @method_decorator(login_required)
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/farm/location/success/')
        return render(request, self.template_name, {'form': form})


class LocationSuccess(TemplateView):
    template_name = 'farm_management/location-success.html'

class SensorDataForm(forms.ModelForm):
    class Meta:
        model = Sensor_Data
        fields = ['location','pH','Moisture','Humidity', 'Temperature','Light','Co2_level','Wind','SunTracking']


class SensorDataCreate(View):
    template_name = 'farm_management/sensor_da-form.html'
    form_class = SensorDataForm
    @method_decorator(login_required)
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/farm/location/sensor/success/')
        return render(request, self.template_name, {'form': form})

class SensorDataView(ListView):
    model = Sensor_Data
    template_name = 'farm_management/sensor_da-view.html'
    @method_decorator(login_required)
    @method_decorator(permission_required('farm.monitor_data'))
    def dispatch(self, request, *args, **kwargs):
        self.sensor_das = Sensor_Data.objects.all().order_by('location')
        return super(SensorDataView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SensorDataView, self).get_context_data(**kwargs)
        context['sensor_das'] =  self.sensor_das
        return context

class MyFarmView(ListView):
    model = Sensor_Data
    template_name = 'farm_management/my_farm-view.html'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.sensor_das = Sensor_Data.objects.all().filter(location__farm__user = request.user)
        return super(MyFarmView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MyFarmView, self).get_context_data(**kwargs)
        context['sensor_das'] =  self.sensor_das
        return context

class SensorSuccess(TemplateView):
    template_name = 'farm_management/sensor_da-success.html'

