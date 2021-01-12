from django.urls import path
try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url

from crop_planning.views import CropPlanCreate,CropPlanView,CropPlanSuccess

urlpatterns = [

    url(r'^crop_plan/$',
    view=CropPlanView.as_view(),
    name='crop_plans'),

    url(r'^crop_plan/new/$',
    view=CropPlanCreate.as_view(),
    name='crop_plan_new'),

    url(r'^crop_plan/success/$',
    view=CropPlanSuccess.as_view(),
    name='crop_plan_success'),



]