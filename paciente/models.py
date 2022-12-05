from unittest.util import _MAX_LENGTH
from django import forms
from django.db import models
from verificacao.validator import validate_cpfrg, validate_digits, validate_sus, validate_no_digits, validate_cep, validate_data, validate_contato, validate_sigla

class Paciente(models.Model):
     Opcoes_Sexo = (
          ("M", "Masculino"),
          ("F", "Feminino")
     )
     Opcoes_Docs = (
        ("CPF", "CPF"),
        ("RG", "RG")
    )

     nome_paciente = models.CharField(max_length=256, validators=[validate_no_digits])
     sexo_paciente = models.CharField(max_length=3, choices=Opcoes_Sexo, blank=False, null=False)
     data_nascimento_paciente = models.DateField(validators=[validate_data])
     municipio_paciente = models.CharField(max_length=256, validators=[validate_no_digits])
     cep_paciente = models.CharField(max_length=8, validators = [validate_cep, validate_digits])
     endereco_paciente = models.CharField(max_length=256, validators = [validate_no_digits])
     bairro_paciente = models.CharField(max_length=256, validators=[validate_no_digits])
     numero_paciente = models.IntegerField()
     estado_paciente = models.CharField(max_length=2, validators=[validate_sigla, validate_no_digits])
     cartao_sus_paciente = models.CharField(primary_key=True,max_length=15, unique = True, error_messages={"unique":"Cartão do SUS já cadastrado, insira outro"}, validators = [validate_digits, validate_sus])
     documento_paciente = models.CharField(max_length=3, choices=Opcoes_Docs, blank=False, null=False)
     numero_do_documento_paciente = models.CharField(max_length = 11, unique = True, error_messages={"unique":"Número de documento já cadastrado, insira outro."}, validators = [validate_cpfrg, validate_digits])
     contato_emergencia_paciente = models.CharField(max_length=11, validators = [validate_digits, validate_contato])



     