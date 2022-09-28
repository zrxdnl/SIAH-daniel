from unittest.util import _MAX_LENGTH
from django.db import models
from verificacao.validator import validate_no_digits, validate_codigoSetor

class Setor(models.Model):
     nome_setor = models.CharField(max_length=256, validators=[validate_no_digits])
     codigo_setor = models.IntegerField(unique= True, validators=[validate_codigoSetor])

def __str__(self) -> str:
          return self.nome_setor

