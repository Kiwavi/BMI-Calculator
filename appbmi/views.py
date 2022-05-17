from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import HeightWeightFillForm
# Create your views here.

class HomePageWithBMICalculation(FormView):
    template_name = 'home.html'
    form_class = HeightWeightFillForm

class CalculatedBMIView(TemplateView):
    template_name = 'calculatedbmi.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        persons_weight = int(self.request.GET.get('weight'))
        persons_height = int(self.request.GET.get('height'))
        persons_height_in_meters_multiplied = (persons_height / 100) ** 2
        body_mass_index = persons_weight / persons_height_in_meters_multiplied
        context['bmi'] = body_mass_index
        if body_mass_index < 18.5:
            context['bmistatus'] = 'You are considered to be underweight.'
        if body_mass_index > 18.5 and body_mass_index < 24.9:
            context['bmistatus'] = 'You are considered to be normal.'
        if body_mass_index > 25.0 and body_mass_index < 29.9:
            context['bmistatus'] = 'You are considered to be overweight.'
        if body_mass_index > 30.0:
            context['bmistatus'] = 'You are considered to be obese.'
        return context
    
#next step is to implement this using htmx and then with react frontend 
