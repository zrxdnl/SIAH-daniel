from django import forms
from django.forms import fields, models
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
     Data_Nascimento_Funcionario = forms.DateField(
          widget=forms.TextInput(
               attrs={"type": "date"}
          )
     )

     class Meta:
          model = Funcionario
          fields = [
               'Nome_Funcionario',
               'CPF_Funcionario',
               'Data_Nascimento_Funcionario',
               'Contato_Funcionario',
               'Endereco_Funcionario',
               'Bairro_Funcionario',
               'Numero_Funcionario',
               'Complemento_Funcionario'
          ]