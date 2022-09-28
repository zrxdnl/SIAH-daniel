from django import forms
from django.forms import fields, models
from .models import Setor

class SetorForm(forms.ModelForm):
     class Meta:
          model = Setor
          fields = ['nome_setor', 'codigo_setor']
          