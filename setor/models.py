from unittest.util import _MAX_LENGTH
from django.db import models

class Setor(models.Model):
     nome_setor = models.CharField(max_length=256)
     codigo_setor = models.IntegerField()

def __str__(self) -> str:
          return self.nome_setor

