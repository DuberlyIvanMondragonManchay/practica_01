from django.forms import ModelForm
from django import forms

from .models import Food
class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name','description','color'] 
        widgets = {
            'color': forms.TextInput(attrs={'placeholder': '#f6bf26'}),
        }
        