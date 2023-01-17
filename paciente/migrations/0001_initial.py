# Generated by Django 4.1.1 on 2023-01-17 19:37

from django.db import migrations, models
import verificacao.validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('nome_paciente', models.CharField(max_length=256, validators=[verificacao.validator.validate_no_digits])),
                ('sexo_paciente', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=3)),
                ('data_nascimento_paciente', models.DateField(validators=[verificacao.validator.validate_data])),
                ('municipio_paciente', models.CharField(max_length=256, validators=[verificacao.validator.validate_no_digits])),
                ('cep_paciente', models.CharField(max_length=8, validators=[verificacao.validator.validate_cep, verificacao.validator.validate_digits])),
                ('endereco_paciente', models.CharField(max_length=256, validators=[verificacao.validator.validate_no_digits])),
                ('bairro_paciente', models.CharField(max_length=256, validators=[verificacao.validator.validate_no_digits])),
                ('numero_paciente', models.IntegerField()),
                ('estado_paciente', models.CharField(max_length=2, validators=[verificacao.validator.validate_sigla, verificacao.validator.validate_no_digits])),
                ('cartao_sus_paciente', models.CharField(error_messages={'unique': 'Cartão do SUS já cadastrado, insira outro'}, max_length=15, unique=True, validators=[verificacao.validator.validate_digits, verificacao.validator.validate_sus])),
                ('numero_do_documento_paciente', models.CharField(error_messages={'unique': 'Número de CPF já cadastrado, insira outro.'}, max_length=11, primary_key=True, serialize=False, unique=True, validators=[verificacao.validator.validate_cpf, verificacao.validator.validate_digits])),
                ('contato_emergencia_paciente', models.CharField(max_length=11, validators=[verificacao.validator.validate_digits, verificacao.validator.validate_contato])),
            ],
        ),
    ]
