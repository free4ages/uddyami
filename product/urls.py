from django.contrib import admin
from django.urls import path
from .views import HomeView,FoodView,FruitsView,VegView,DairyView,TextileView,TailorView,BeverageView,JobsView,ServicesView,\
RentVehicleView,LoanView,ConstructionView,ConsultantView\
,MakhanaView,JaggeryView,PulsesView,MaizeView,FoodProcessingView \
,MangoView,BananaView,LitchiView,GuavaView,PapayaView,\
TomatoView, BrinjalView,MirchiView,CauliflowerView,\
MilkView, GheeView, PaneerView, PedaView,\
TeaView,CoffeeView,DrinksView,\
BhagalpuriChadarView,LedLightView,FisheriesView,FishingPondView,MiscellaneousView

try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url


urlpatterns = [
        url(r'^$',
        view=HomeView.as_view(),
        name='home'),

        url(r'^food/$',
        view=FoodView.as_view(),
        name='food'),

        url(r'^food/makhana/$',
        view=MakhanaView.as_view(),
        name='makhana'),

        url(r'^food/jaggery/$',
        view=JaggeryView.as_view(),
        name='jaggery'),

        url(r'^food/pulses/$',
        view=PulsesView.as_view(),
        name='pulses'),

        url(r'^food/maize/$',
        view=MaizeView.as_view(),
        name='maize'),

        url(r'^food/processing/$',
        view=FoodProcessingView.as_view(),
        name='food_processing'),

        url(r'^fruits/$',
        view=FruitsView.as_view(),
        name='fruits'),

        url(r'^fruits/mango/$',
        view=MangoView.as_view(),
        name='mango'),

          url(r'^fruits/banana/$',
        view=BananaView.as_view(),
        name='banana'),

        url(r'^fruits/litchi/$',
        view=LitchiView.as_view(),
        name='litchi'),

        url(r'^fruits/papaya/$',
        view=PapayaView.as_view(),
        name='papaya'),

         url(r'^fruits/guava/$',
        view=GuavaView.as_view(),
        name='guava'),

        url(r'^veg/$',
        view=VegView.as_view(),
        name='vegetables'),

        url(r'^veg/tomato/$',
        view=TomatoView.as_view(),
        name='tomato'),

         url(r'^veg/brinjal/$',
        view=BrinjalView.as_view(),
        name='brinjal'),

         url(r'^veg/mirchi/$',
        view=MirchiView.as_view(),
        name='mirchi'),

         url(r'^veg/cauliflower/$',
        view=CauliflowerView.as_view(),
        name='cauliflower'),

        url(r'^dairy/$',
        view=DairyView.as_view(),
        name='dairy'),

        url(r'^dairy/milk/$',
        view=MilkView.as_view(),
        name='milk'),

        url(r'^dairy/ghee/$',
        view=GheeView.as_view(),
        name='ghee'),

        url(r'^dairy/paneer/$',
        view=PaneerView.as_view(),
        name='paneer'),

        url(r'^dairy/peda/$',
        view=PedaView.as_view(),
        name='peda'),

        url(r'^beverage/$',
        view=BeverageView.as_view(),
        name='beverage'),

        url(r'^beverage/tea/$',
        view=TeaView.as_view(),
        name='tea'),

        url(r'^beverage/coffee/$',
        view=CoffeeView.as_view(),
        name='coffee'),

        url(r'^beverage/drinks/$',
        view=DrinksView.as_view(),
        name='drinks'),

        url(r'^textile/$',
        view=TextileView.as_view(),
        name='textile'),

        url(r'^textile/bhagalpuriChadar/$',
        view=BhagalpuriChadarView.as_view(),
        name='bhagalpurichadar'),

        url(r'^services/tailor/$',
        view=TailorView.as_view(),
        name='tailor'),

         url(r'^services/$',
        view=ServicesView.as_view(),
        name='services'),

        url(r'^services/jobs/$',
        view=JobsView.as_view(),
        name='jobs'),

        url(r'^services/rent_vehicle/$',
        view=RentVehicleView.as_view(),
        name='rent_vehicle'),

        url(r'^services/loan/$',
        view=LoanView.as_view(),
        name='loan'),

        url(r'^services/consultant/$',
        view=ConsultantView.as_view(),
        name='consultant'),

        url(r'^services/construction/$',
        view=ConstructionView.as_view(),
        name='construction'),

        url(r'^services/miscellaneous/$',
        view=MiscellaneousView.as_view(),
        name='miscellaneous'),

        url(r'^led/$',
        view=LedLightView.as_view(),
        name='led'),

        url(r'^fisheries/$',
        view=FisheriesView.as_view(),
        name='fisheries'),

         url(r'^fisheries/fishing_pond/$',
        view=FishingPondView.as_view(),
        name='fishing_pond'),

]