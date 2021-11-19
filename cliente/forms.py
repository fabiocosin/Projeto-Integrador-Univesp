from django import forms
from django.forms import fields, models
from .models import cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nome_completo', 'data_nascimento', ]