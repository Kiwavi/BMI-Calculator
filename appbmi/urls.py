from django.urls import path
from . import views

urlpatterns = [
    path('', views.BMICalculateSamePage.as_view(),name='bmipage'),
    path('bmicalc', views.calculate_bmi, name='bmicalc'),
]
