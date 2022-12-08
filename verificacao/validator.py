from django.core.exceptions import ValidationError
from datetime import date 
import datetime

 # --- General Validators --- #

def validate_data(value):
     data_user = value
     data_server = datetime.datetime.today()
     if str(data_user) > str(data_server):
          raise ValidationError('Data Inválida')
     else:
          return value 

def validate_digits(value): 
     if not str(value).isdigit(): 
          raise ValidationError('Este campo só aceita números') 
     else: 
          return value 

def validate_no_digits(value): 
     if any(n.isdigit() for n in value): 
          raise ValidationError('Este campo não aceita números') 
     else: 
          return value 

def validate_cnes(value):
     if len(value) != 7:
          raise ValidationError('O campo exige 7 dígitos')
     else:
          return value

def validate_codigoSetor(value):
     if (value<0) or (value>99):
          raise ValidationError('O campo deve ter no mínimo 2 dígitos')
     else:
          return value

def validate_cep(value):
     if len(value) < 8:
          raise ValidationError('O campo deve conter 8 dígitos')

def validate_jaCadastrado(value):
     if value.filter:
          pass
def validate_contato(value):
     if len(value) != 11:
          raise ValidationError('Digite um telefone válido')
     else:
          return value
'''def validate_data(value): 
     if len(value) != 10: 
          raise ValidationError('A data está errada.') 
     else: 
          return value 

def validate_year(value): 
     if len(value) != 4: 
          raise ValidationError('São necessários 4 digitos.') 
     else: 
          return value'''

 # --- Documents Validators --- # 
def validate_cnpj(value): 
     if len(value) != 14: 
          raise ValidationError('O campo necessita 14 números') 
     else: 
          return value

def validate_sigla(value):
     if len(value) != 2:
          raise ValidationError('Informe a sigla do estado')
     else:
          return value
def validate_cpfrg(value):
     if ((len(value) != 7) and (len(value) != 11)):
          raise ValidationError('Insira CPF ou RG válido(11 dígitos no caso de CPF, ou 7 no caso de RG)')
     else:
          return value
def validate_sus(value):
     if len(value) != 15:
          raise ValidationError('Insira pelo menos 15 dígitos')
     else:
          return value

'''def validate_Data(value):
     dividir = value.split()
     if int(dividir[0] + dividir[1]) > 31:
          raise ValidationError('Data inválida, digite a data em forma de (dia/mês/ano)')
     elif int(dividir[3]+dividir[4]) > 12:
          raise ValidationError('Data inválida, digite a data em forma de (dia/mês/ano)')
     else: 
          return value'''
def validate_cpf(value): 
     if len(value) != 11: 
          raise ValidationError('O campo necessita 11 números') 
     else: 
          return value
def validate_localizacao(value): 
     if len(value) != 10: 
          raise ValidationError('O campo necessita de 10 números') 
     else: 
          return value
def validate_numeroficha(value):
     if len(value) != 5: 
          raise ValidationError('O campo necessita de 5 números') 
     else: 
          return value