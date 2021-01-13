from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView,DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.base import TemplateView
# Create your views here.
from django import forms
from .cropBudgetCalc import CropBudgetCalc

from crop_planning.models import CropPlan,CropBudget

class CropBudgetForm(forms.ModelForm):
    class Meta:
        model=CropBudget
        fields = "__all__"

class CropBudgetView(View):
    template_name = 'crop/crop_budget-form.html'
    form_class = CropBudgetForm

    def get(self,request,*args,**kwargs):
        instance = None
        results = []
        form = None
        crops = CropBudget.objects.order_by('sticky')
        if 'results' in kwargs:
            results = kwargs['results']
        if 'form_data' in kwargs:
            form = kwargs['form_data']
        elif 'crop_slug' in kwargs:
            form = CropBudget.objects.get(crop_slug=kwargs['crop_slug'])
        return render(request,self.template_name,{'form':form,'crops':crops,'results':results})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            kwargs['form_data'] = form.cleaned_data
            kwargs['results'] = CropBudgetCalc(**kwargs['form_data']).profitLossData()
        return self.get(request,*args,**kwargs)

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
