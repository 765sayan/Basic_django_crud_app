from django.core import validators
from django import forms
from matplotlib import widgets
from .models import User



class StudentRegistration(forms.ModelForm): #This is a Django ModelForm
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        }