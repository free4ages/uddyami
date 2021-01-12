from django.urls import path
try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url

from farm_management.views import FarmList,FarmCreate,FarmSuccess,LocationCreate,LocationSuccess,SensorDataCreate,SensorDataView,SensorSuccess,\
MyFarmView

urlpatterns = [

    url(r'^farm/$',
    view=FarmList.as_view(),
    name='farms'),

    url(r'^farm/new/$',
    view=FarmCreate.as_view(),
    name='farm_new'),

    url(r'^farm/success/$',
    view=FarmSuccess.as_view(),
    name='farm_success'),

    url(r'^farm/location/new/$',
    view=LocationCreate.as_view(),
    name='location_new'),

    url(r'^farm/location/success/$',
    view=LocationSuccess.as_view(),
    name='location_success'),

    url(r'^farm/location/sensor_da/$',
    view=SensorDataView.as_view(),
    name='sensor_da_view'),

    url(r'^farm/my_farm/$',
    view=MyFarmView.as_view(),
    name='my_farm_view'),

    url(r'^farm/location/sensor_da/new/$',
    view=SensorDataCreate.as_view(),
    name='sensor_da_create'),

    url(r'^farm/location/sensor_da/success/$',
    view=SensorSuccess.as_view(),
    name='sensor_success'),

]