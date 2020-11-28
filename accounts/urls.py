from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
        path('accounts/login/', views.index, name="my-login"),
        path('accounts/about/', views.about, name="about"),
        path('accounts/sign_up/',views.sign_up,name="sign-up"),
]