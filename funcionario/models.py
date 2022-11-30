from django.db import models
from verificacao.validator import validate_no_digits, validate_digits, validate_contato, validate_data, validate_cpf
class Funcionario(models.Model):
     Nome_Funcionario = models.CharField(max_length=256, validators=[validate_no_digits])
     CPF_Funcionario = models.CharField(unique = True,max_length=11,error_messages={"unique":"CPF já cadastrado, insira outro"}, validators = [validate_digits, validate_cpf])
     Data_Nascimento_Funcionario = models.DateField(validators=[validate_data])
     Contato_Funcionario = models.CharField(max_length=11, validators=[validate_digits, validate_contato])
     Endereco_Funcionario = models.CharField(max_length=256, validators=[validate_no_digits])
     Bairro_Funcionario = models.CharField(max_length=256, validators=[validate_no_digits])
     Numero_Funcionario = models.CharField(max_length=256, validators=     [validate_digits])
     Complemento_Funcionario = models.CharField(max_length=256)
     #Login_Funcionario = models.
     #Senha_Funcionario = models.