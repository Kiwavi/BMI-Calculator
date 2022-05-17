from django import forms

class HeightWeightFillForm(forms.Form):
    weight = forms.IntegerField(min_value=1)
    height = forms.IntegerField(min_value=1)
    


