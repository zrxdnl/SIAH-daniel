from django import forms
from django.db import models
from paciente.models import Paciente
from verificacao.validator import validate_data, validate_sus, validate_digits, validate_localizacao, validate_numeroficha
class Fichamedica(models.Model):
     Numero_Ficha = models.CharField(max_length=5, unique = True, error_messages={"unique":"Número de Ficha já cadastrado, insira outro"}, validators=[validate_digits, validate_numeroficha])
     Numero_SUS = models.ForeignKey(Paciente,null = False, on_delete=models.CASCADE)
     Data_Admissao = models.DateTimeField(validators=[validate_data])
     Hora_Admissao = models.TimeField()
     Localizacao_Fisica = models.CharField(max_length=9, validators=[validate_localizacao])