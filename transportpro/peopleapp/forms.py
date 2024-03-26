from django import forms
from .models import People


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = "__all__"

        widgets = {
            "people_name": forms.TextInput(attrs={'class': 'form-controls'}),
            "distination_location": forms.Select(attrs={'class': 'form-controls'}),
            "weight": forms.NumberInput(attrs={'class': 'form-controls'}),
            "price": forms.NumberInput(attrs={'class': 'form-controls'}),
            "payment_mode": forms.Select(attrs={'class': 'form-controls'}),
        }
