from django.urls import path
from . import views

urlpatterns = [
    #path('', HomePageWithBMICalculation.as_view(), name='home'),
    #path('bmiresult', views.CalculatedBMIView.as_view(),name='bmiresult'),
    path('', views.BMICalculateSamePage.as_view(),name='bmipage'),
    path('bmicalc', views.calculate_bmi, name='bmicalc'),
]
