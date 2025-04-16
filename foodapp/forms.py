from django import forms
from .models import *


class InputForm(forms.Form):
    ingredients = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter ingredients separated by commas'}))
