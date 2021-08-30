from django import forms
from .models import Order
class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        widgets = {"intake_date_and_time": forms.DateTimeInput(attrs={'type':'datetime-local'}) }
        fields = '__all__'
    
