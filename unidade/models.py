from django.db import models
from verificacao.validator import validate_no_digits, validate_digits, validate_cep, validate_cnes, validate_cnpj, validate_sigla

class Unidade(models.Model):
     nome_unidade = models.CharField(max_length=256, validators=[validate_no_digits])
     cnes = models.CharField(unique=True, error_messages={"unique":"CNES já cadastrado, insira outro."}, max_length=7, validators=[validate_digits, validate_cnes])
     cnpj = models.CharField(unique=True, error_messages={"unique":"CNPJ já cadastrado, insira outro."}, max_length=14, validators=[validate_cnpj, validate_digits])
     orgaoEmissor_unidade = models.CharField(max_length=256, validators=[validate_no_digits])
     endereco_unidade = models.CharField(max_length=256)
     bairro_unidade = models.CharField(max_length=256)
     numero_unidade = models.IntegerField()
     estado_unidade = models.CharField(max_length=10, validators=[validate_no_digits, validate_sigla])
     cep_unidade = models.CharField(max_length=8, validators=[validate_digits, validate_cep])

     def __str__(self) -> str:
          return self.nome_unidade


