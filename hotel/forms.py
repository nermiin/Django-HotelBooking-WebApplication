from django import forms
from .models import Hotel

class HotelCreate(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
