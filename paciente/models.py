from unittest.util import _MAX_LENGTH
from django.db import models

class Paciente(models.Model):
     nome_paciente = models.CharField(max_length=256)
     sexo_paciente = models.CharField(max_length=1)
     datanascimento_paciente = models.DateField()
     municipio_paciente = models.CharField(max_length=256)
     cep_paciente = models.CharField(max_length=8)
     endereco_paciente = models.CharField(max_length=256)
     bairro_paciente = models.CharField(max_length=256)
     numero_paciente = models.IntegerField()
     estado_paciente = models.CharField(max_length=10)
     cartaosus_paciente = models.CharField(max_length=15)
     documento_paciente = models.CharField(max_length=256)
     numerodocumento_paciente = models.CharField(max_length = 11)
     contatoemergencia_paciente = models.CharField(max_length=11)
     