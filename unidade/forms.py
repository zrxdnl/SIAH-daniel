from socket import fromshare
from django import forms
from .models import Unidade

class UnidadeForm(forms.ModelForm):
     class Meta:
          model = Unidade
          fields = ['nome_unidade', 'cnes', 'cnpj', 'orgaoEmissor_unidade', 'endereco_unidade', 'bairro_unidade', 'numero_unidade', 'estado_unidade', 'cep_unidade']