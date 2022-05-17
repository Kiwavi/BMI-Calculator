from django.urls import path
from appbmi.views import HomePageWithBMICalculation
from . import views

urlpatterns = [
    path('', HomePageWithBMICalculation.as_view(), name='home'),
    path('bmiresult', views.CalculatedBMIView.as_view(),name='bmiresult'),
]
