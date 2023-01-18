from django import forms
from django.db import models
from paciente.models import Paciente
from verificacao.validator import validate_hora, validate_data, validate_digits, validate_localizacao, validate_numerodocumento
class Fichamedica(models.Model): 
     Numero_Ficha = models.CharField(max_length=5, unique = True, error_messages={"unique":"Número de Ficha já cadastrado, insira outro"}, validators=[validate_digits, validate_numerodocumento])
     Numero_CPF = models.ForeignKey(Paciente,null = False, on_delete=models.CASCADE, related_name="CPF") 
     Data_Admissao = models.DateTimeField(validators=[validate_data])
     Hora_Admissao = models.TimeField(validators=[validate_hora])
     Municipio = models.CharField(max_length=30)
     Localizacao_Fisica = models.CharField(max_length=9, validators=[validate_localizacao])
     def save(self,*args, **kwargs):
          self.Municipio = self.Numero_CPF.municipio_paciente
          data = str(self.Data_Admissao).split('-')
          ano = data[0]
          mes = data[1]
          self.Localizacao_Fisica = ano+mes
          super(Fichamedica, self).save(*args,**kwargs)