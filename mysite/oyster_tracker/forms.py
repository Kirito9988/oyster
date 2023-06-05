from django import forms
from .models import OysterPackage


class OysterPackageForm(forms.ModelForm):
    received_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}))
    harvest_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}))

    class Meta:
        model = OysterPackage
        fields = ['received_date', 'harvest_date', 'full_name', 'note_image']
