from unittest.util import _MAX_LENGTH
from django import forms
from django.db import models
from verificacao.validator import validate_cpf, validate_digits, validate_sus, validate_no_digits, validate_cep, validate_data, validate_contato, validate_sigla

class Paciente(models.Model):
     Opcoes_Sexo = (
          ("M", "Masculino"),
          ("F", "Feminino")
     )
     Opcoes_Docs = (
        ("CPF", "CPF"),
        ("RG", "RG")
    )

     Nome = models.CharField(max_length=256, validators=[validate_no_digits])
     Sexo = models.CharField(max_length=3, choices=Opcoes_Sexo, blank=False, null=False)
     Data_Nascimento = models.DateField(validators=[validate_data])
     Municipio_Paciente = models.CharField(max_length=256, validators=[validate_no_digits])
     cep_paciente = models.CharField(max_length=8, validators = [validate_cep, validate_digits])
     endereco_paciente = models.CharField(max_length=256, validators = [validate_no_digits])
     bairro_paciente = models.CharField(max_length=256, validators=[validate_no_digits])
     numero_paciente = models.IntegerField()
     estado_paciente = models.CharField(max_length=2, validators=[validate_sigla, validate_no_digits])
     Cartao_SUS = models.CharField(max_length=15, unique = True, error_messages={"unique":"Cartão do SUS já cadastrado, insira outro"}, validators = [validate_digits, validate_sus])
     cpf_paciente = models.CharField(primary_key=True, max_length = 11, unique = True, error_messages={"unique":"Número de CPF já cadastrado, insira outro."}, validators = [validate_cpf, validate_digits])
     Contato_Emergencia = models.CharField(max_length=11, validators = [validate_digits, validate_contato])

     def __str__(self):
          return self.cpf_paciente
     
     def getNome(self):
          return self.Nome
     def getCPF(self):
          return self.cpf_paciente


     