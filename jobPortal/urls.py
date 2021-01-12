from django.urls import path
try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url

from jobPortal.views import JobItemList,JobItemCreate,JobPostSuccess

urlpatterns = [
    url(r'^job/$',
    view=JobItemList.as_view(),
    name='job_list'),

    url(r'^job/new/$',
    view=JobItemCreate.as_view(),
    name='job_new'),

    url(r'^job/success/$',
    view=JobPostSuccess.as_view(),
    name='job_post_success'),
]