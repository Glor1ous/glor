from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['email', 'phone']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}),
        }
