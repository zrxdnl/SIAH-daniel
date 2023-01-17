from django import forms
from django.forms import fields, models
from .models import Paciente

class PacienteForm(forms.ModelForm):
     data_nascimento_paciente = forms.DateField(
          widget=forms.TextInput(
               attrs={"type": "date"}
          )
     )

     class Meta:
          model = Paciente
          fields = ['nome_paciente', 'sexo_paciente', 'data_nascimento_paciente', 'municipio_paciente', 'cep_paciente', 'endereco_paciente', 'bairro_paciente', 'numero_paciente', 'estado_paciente', 'cartao_sus_paciente', 'numero_do_documento_paciente', 'contato_emergencia_paciente']