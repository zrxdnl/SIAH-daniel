from django import forms
from django.forms import fields, models
from .models import Fichamedica

class FichamedicaForm(forms.ModelForm):
     Data_Admissao = forms.DateTimeField(
          widget=forms.TextInput(
               attrs={"type": "date"}
          )
     )

     Hora_Admissao = forms.TimeField(
          widget=forms.TextInput(
               attrs={"type": "time"}
          )
     )

     class Meta:
          model = Fichamedica
          fields = [
               'Numero_Ficha',
               'Numero_CPF',
               'Data_Admissao',
               'Hora_Admissao'
          ]