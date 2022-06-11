from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import HeightWeightFillForm
import json
# Create your views here.

#for htmx, contains form
class BMICalculateSamePage(TemplateView):
    template_name = 'bmiresult.html'

#for htmx 
def calculate_bmi(request):
    persons_weight = request.GET.get('weight')
    persons_height = request.GET.get('height')
    persons_height_in_meters_multiplied = (int(persons_height) / 100) ** 2
    body_mass_index = int(persons_weight) / persons_height_in_meters_multiplied
    if body_mass_index < 18.5:
        bmistatus = 'You are considered to be underweight.'
    if body_mass_index > 18.5 and body_mass_index < 24.9:
        bmistatus = 'You are considered to be normal.'
    if body_mass_index > 25.0 and body_mass_index < 29.9:
        bmistatus = 'You are considered to be overweight.'
    if body_mass_index > 30.0:
        bmistatus = 'You are considered to be obese.'
    return render(request,'partials/bmiresult.html',{'bmi':body_mass_index,'bmistatus':bmistatus})


#next step is to implement this using htmx and then with react frontend 

'''
Should be like the one for adding films. 
The form template should be there with the form to calculate BMI and then a div below to show the result and also the BMI status. In the partials template, It should show ‘0.00’ if there’s no context, then when someone calculates using hx-get, send that request to the calculating view then return the results to partials and then load it.
'''



