from django.db import models

class Unidade(models.Model):
     nome_unidade = models.CharField(max_length=256)
     cnes = models.CharField(max_length=14)
     cnpj = models.CharField(max_length=14)
     orgaoEmissor_unidade = models.CharField(max_length=256)
     endereco_unidade = models.CharField(max_length=256)
     bairro_unidade = models.CharField(max_length=256)
     numero_unidade = models.IntegerField()
     estado_unidade = models.CharField(max_length=10)
     cep_unidade = models.CharField(max_length=8)

     def __str__(self) -> str:
          return self.nome_unidade


