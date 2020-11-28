from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required,permission_required
from .forms import SignUpForm
from django.contrib import messages
from django.utils.decorators import method_decorator



@login_required
def index(request):
    return render(request,'accounts/index.html')

def about(request):
    return render(request,'accounts/about.html')

def sign_up(request):
    context = {}
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request,'accounts/index.html')
    else:
        form = SignUpForm()
    context['form']=form
    return render(request, 'registration/sign_up.html',context)