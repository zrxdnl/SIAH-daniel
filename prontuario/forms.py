from django import forms
from django.forms import fields, models
from .models import Prontuario

class ProntuarioForm(forms.ModelForm):
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
          model = Prontuario
          fields = [
               'Numero_Prontuario',
               'Numero_CPF',
               'Codigo_Setor',
               'Medico_Responsavel',
               'Data_Admissao',
               'Hora_Admissao',
               'Localizacao_Fisica'
          ]