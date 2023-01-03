from django.db import models
from django import forms
from paciente.models import Paciente
from setor.models import Setor
# Create your models here.
class Prontuario(models.Model):
     Numero_Prontuario = models.CharField(max_length=5, unique = True, error_messages={"unique":"Número de Prontuário já cadastrado, insira outro"})
     Numero_SUS = models.ForeignKey(Paciente,null = False, on_delete=models.CASCADE)
     Codigo_Setor = models.ForeignKey(Setor,null = False, on_delete=models.CASCADE) 
     Medico_Responsavel = models.CharField(max_length=256)
     Data_Admissao = models.DateTimeField()
     Hora_Admissao = models.TimeField()
     Localizacao_Fisica = models.CharField(max_length=9)
     