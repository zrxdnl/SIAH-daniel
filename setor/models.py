from unittest.util import _MAX_LENGTH
from django.db import models
from verificacao.validator import validate_no_digits, validate_codigoSetor, validate_digits

class Setor(models.Model):  
     nome_setor = models.CharField(max_length=256, validators=[validate_no_digits])
     codigo_setor = models.IntegerField(primary_key = True, unique= True, error_messages={"unique":"ID já cadastrado, insira outro."}, validators=[validate_codigoSetor,validate_digits])

     def __str__(self):
          return str(self.codigo_setor)
          
     def getNome_setor(self):
          return self.nome_setor
