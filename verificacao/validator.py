from django.core.exceptions import ValidationError 
'''from datetime import date''' 

 # --- General Validators --- # 
def validate_digits(value): 
     if not value.isdigit(): 
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

'''def validate_cpf(value): 
     if len(value) != 11: 
          raise ValidationError('O campo necessita 11 números') 
     else: 
          return value'''

