# Create your views here.
from django.shortcuts import render
import re
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from member.models import Member

class HomeView(TemplateView):
    template_name = 'home.html'

class FoodView(TemplateView):
    template_name = 'food.html'

class FruitsView(TemplateView):
    template_name = 'fruits.html'

class VegView(TemplateView):
    template_name = 'veg.html'

class DairyView(TemplateView):
    template_name = 'dairy.html'

class TextileView(TemplateView):
    template_name = 'textile.html'

class BeverageView(TemplateView):
    template_name = 'beverage.html'

class ServicesView(TemplateView):
    template_name = 'services.html'

class JobsView(TemplateView):
    template_name = 'services/jobs.html'

class FisheriesView(TemplateView):
    template_name = 'fisheries.html'

class MiscellaneousView(TemplateView):
    template_name = 'services/miscellaneous.html'
     # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                match = re.search('miscellaneous', str(prod.sub_category))
                if match:
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district, x.state) )
        self.members = mems
        return super(MiscellaneousView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MiscellaneousView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class FishingPondView(TemplateView):
    template_name = 'fisheries/fishing_pond.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'fishingpond':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district, x.state) )
        self.members = mems
        return super(FishingPondView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FishingPondView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class MakhanaView(TemplateView):
    template_name = 'food/makhana.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'makhana':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(MakhanaView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MakhanaView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class JaggeryView(TemplateView):
    template_name = 'food/jaggery.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'jaggery':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(JaggeryView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(JaggeryView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class PulsesView(TemplateView):
    template_name = 'food/pulses.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'pulses':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(PulsesView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PulsesView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class FoodProcessingView(TemplateView):
    template_name = 'food/processing.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'food processing':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(FoodProcessingView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FoodProcessingView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class MaizeView(TemplateView):
    template_name = 'food/maize.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'maize':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(MaizeView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MaizeView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context


class MangoView(TemplateView):
    template_name = 'fruits/mango.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'mango':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(MangoView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MangoView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class BananaView(TemplateView):
    template_name = 'fruits/banana.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'banana':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(BananaView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BananaView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class LitchiView(TemplateView):
    template_name = 'fruits/litchi.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'litchi':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(LitchiView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LitchiView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class GuavaView(TemplateView):
    template_name = 'fruits/guava.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'guava':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(GuavaView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GuavaView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class PapayaView(TemplateView):
    template_name = 'fruits/papaya.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'papaya':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(PapayaView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PapayaView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class TomatoView(TemplateView):
    template_name = 'vegetables/tomato.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'tomato':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(TomatoView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TomatoView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class BrinjalView(TemplateView):
    template_name = 'vegetables/brinjal.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'brinjal':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(BrinjalView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BrinjalView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class MirchiView(TemplateView):
    template_name = 'vegetables/mirchi.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'mirchi':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(MirchiView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MirchiView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class CauliflowerView(TemplateView):
    template_name = 'vegetables/cauliflower.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'cauliflower':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(CauliflowerView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CauliflowerView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class MilkView(TemplateView):
    template_name = 'dairy/milk.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'milk':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(MilkView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MilkView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class GheeView(TemplateView):
    template_name = 'dairy/ghee.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'ghee':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(GheeView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GheeView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class PaneerView(TemplateView):
    template_name = 'dairy/paneer.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'paneer':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(PaneerView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PaneerView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class PedaView(TemplateView):
    template_name = 'dairy/peda.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'peda':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(PedaView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PedaView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class TeaView(TemplateView):
    template_name = 'beverage/tea.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'tea':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(TeaView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TeaView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class CoffeeView(TemplateView):
    template_name = 'beverage/coffee.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'coffee':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(CoffeeView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CoffeeView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class DrinksView(TemplateView):
    template_name = 'beverage/drinks.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'drinks':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(DrinksView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DrinksView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class BhagalpuriChadarView(TemplateView):
    template_name = 'textile/bhagalpurichadar.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'bhagalpurichadar':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(BhagalpuriChadarView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BhagalpuriChadarView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class TailorView(TemplateView):
    template_name = 'services/tailor_stitch.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'tailor':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(TailorView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TailorView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context


class ConstructionView(TemplateView):
    template_name = 'construction.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                match = re.search('Construction', str(prod.category))
                if match:
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(ConstructionView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ConstructionView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class LoanView(TemplateView):
    template_name = 'services/loan.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'loan':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(LoanView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LoanView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class LedLightView(TemplateView):
    template_name = 'led.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'led':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(LedLightView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LedLightView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class RentVehicleView(TemplateView):
    template_name = 'services/rent_vehicle.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                match = re.search('rent_vehicle', str(prod.sub_category))
                if match:
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(RentVehicleView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RentVehicleView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context

class ConsultantView(TemplateView):
    template_name = 'services/consultant.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        mems = []
        for mem in Member.objects.exclude(active = 'False'):
            for prod in mem.products.all():
                if prod.title.lower() == 'consultant':
                    mems.append(mem)

        # self.members = sorted(mems, key=lambda x:(x.district,x.state) )
        self.members = mems
        return super(ConsultantView, self)\
                .dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ConsultantView, self).get_context_data(**kwargs)
        context['members'] =  self.members
        return context