from django import forms
from .models import news

class newsForm(forms.Form):
    query = forms.CharField(widget=forms.HiddenInput(), required=False)
