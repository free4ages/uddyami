from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView,DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.base import TemplateView
# Create your views here.
from django import forms

from crop_planning.models import CropPlan

class CropPlanForm(forms.ModelForm):
    class Meta:
        model = CropPlan
        fields = ['plan','bigha','kattha','katthaToSqFeet','area','season','crop','seeding','seeding_date','fertigation_plan','plant_protection_plan','weeding_plan',\
        'labour_planning']

class CropPlanCreate(View):
    template_name = 'crop/crop_plan-form.html'
    form_class = CropPlanForm

    @method_decorator(login_required)
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/crop_plan/success/')
        return render(request, self.template_name, {'form': form})

class CropPlanView(ListView):
    model = CropPlan
    template_name = 'crop/crop_plan-view.html'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.crop_plans = CropPlan.objects.filter(user = request.user)
        return super(CropPlanView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CropPlanView, self).get_context_data(**kwargs)
        context['crop_plans'] =  self.crop_plans
        return context

class CropPlanSuccess(TemplateView):
    template_name = 'crop/crop_plan-success.html'