from django.urls import path
try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url

from saleitem.views import SaleItemList,SaleItemCreate,SaleSuccess

urlpatterns = [
    url(r'^sale/$',
    view=SaleItemList.as_view(),
    name='sales'),

    url(r'^sale/new$',
    view=SaleItemCreate.as_view(),
    name='sale_new'),

    url(r'^sale/success/$',
    view=SaleSuccess.as_view(),
    name='sale_success'),
]

