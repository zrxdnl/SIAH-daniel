from django import forms
from django.forms import fields, models
from .models import Fichamedica

class FichamedicaForm(forms.ModelForm):
     Data_Hora_Admissao = forms.DateTimeField(
          widget=forms.TextInput(
               attrs={"type": "date"}
          )
     )

     

     class Meta:
          model = Fichamedica
          fields = [
               'Numero_Ficha',
               'Numero_SUS',
               'Data_Hora_Admissao',
               'Localizacao_Fisica'
          ]