from django import forms
from django.forms import fields, models
from .models import Paciente

class PacienteForm(forms.ModelForm):
     Data_Nascimento = forms.DateField(
          widget=forms.TextInput(
               attrs={"type": "date"}
          )
     )

     class Meta:
          model = Paciente
          fields = ['Nome', 'Sexo', 'Data_Nascimento', 'Municipio_Paciente', 'cep_paciente', 'endereco_paciente', 'bairro_paciente', 'numero_paciente', 'estado_paciente', 'Cartao_SUS', 'cpf_paciente', 'Contato_Emergencia']