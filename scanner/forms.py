from django import forms
from .models import *


class Loader(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'img']

