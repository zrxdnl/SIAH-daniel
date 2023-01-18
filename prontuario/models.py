from django.db import models
from django import forms
from paciente.models import Paciente
from setor.models import Setor
from verificacao.validator import validate_hora, validate_no_digits, validate_data, validate_digits, validate_localizacao, validate_numerodocumento
# Create your models here.
class Prontuario(models.Model):
     Numero_Prontuario = models.CharField(max_length=5, unique = True, error_messages={"unique":"Número de Prontuário já cadastrado, insira outro"}, validators=[validate_numerodocumento, validate_digits])
     Numero_CPF = models.ForeignKey(Paciente,null = False, on_delete=models.CASCADE)
     Codigo_Setor = models.ForeignKey(Setor,null = False, on_delete=models.CASCADE) 
     Medico_Responsavel = models.CharField(max_length=256, validators=[validate_no_digits])
     Data_Admissao = models.DateTimeField(validators=[validate_data])
     Hora_Admissao = models.TimeField(validators=[validate_hora])
     Localizacao_Fisica = models.CharField(max_length=9, validators=[validate_localizacao]) 
     def save(self,*args, **kwargs): 
          data = str(self.Data_Admissao).split('-')
          ano = data[0]
          mes = data[1]
          setor = str(self.Codigo_Setor)
          self.Localizacao_Fisica = ano+mes+setor
          super(Prontuario, self).save(*args,**kwargs)