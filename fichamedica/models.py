from django import forms
from django.db import models
from paciente.models import Paciente
from verificacao.validator import validate_data
class Fichamedica(models.Model):
     Numero_Ficha = models.CharField(max_length=5, unique = True, error_messages={"unique":"Número de Ficha já cadastrado, insira outro"})
     Numero_SUS = models.ForeignKey(Paciente,null = False, on_delete=models.CASCADE)
     Data_Hora_Admissao = models.DateTimeField()
     Localizacao_Fisica = models.CharField(unique=True,max_length=10, error_messages={'unique':"Localização já cadastrada, insira outra"})