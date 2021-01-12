from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.views.generic.base import TemplateView


from django import forms

from jobPortal.models import JobPost

class JobPostForm(forms.ModelForm):
    mobile = forms.CharField(max_length=10)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    class Meta:
        model = JobPost
        fields = ['job_title','company_name','salary','qualification','description','email','mobile','whatsapp','location','city','state','whatsapp_active']

class JobItemList(ListView):
    queryset = JobPost.objects.exclude(active = 'False').order_by('sticky','date_added')
    template_name = 'job/jobitem-list.html'
    context_object_name = 'jobitems'

class JobItemCreate(View):
    template_name = 'job/jobitem-form.html'
    form_class = JobPostForm
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/job/success/')
        return render(request, self.template_name, {'form': form})

class JobPostSuccess(TemplateView):
    template_name = 'job/job_post_item-success.html'

