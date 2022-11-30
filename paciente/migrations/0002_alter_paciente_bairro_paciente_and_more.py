# Generated by Django 4.1.1 on 2022-11-17 12:55

from django.db import migrations, models
import verificacao.validator


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='bairro_paciente',
            field=models.CharField(max_length=256, validators=[verificacao.validator.validate_no_digits]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cartao_sus_paciente',
            field=models.CharField(error_messages={'unique': 'Cartão do SUS já cadastrado, insira outro'}, max_length=15, unique=True, validators=[verificacao.validator.validate_digits, verificacao.validator.validate_sus]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cep_paciente',
            field=models.CharField(max_length=8, validators=[verificacao.validator.validate_cep, verificacao.validator.validate_digits]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='contato_emergencia_paciente',
            field=models.CharField(max_length=11, validators=[verificacao.validator.validate_digits, verificacao.validator.validate_contato]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_nascimento_paciente',
            field=models.DateField(validators=[verificacao.validator.validate_data]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='documento_paciente',
            field=models.CharField(choices=[('CPF', 'CPF'), ('RG', 'RG')], max_length=3),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='endereco_paciente',
            field=models.CharField(max_length=256, validators=[verificacao.validator.validate_no_digits]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estado_paciente',
            field=models.CharField(max_length=2, validators=[verificacao.validator.validate_sigla, verificacao.validator.validate_no_digits]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='municipio_paciente',
            field=models.CharField(max_length=256, validators=[verificacao.validator.validate_no_digits]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nome_paciente',
            field=models.CharField(max_length=256, validators=[verificacao.validator.validate_no_digits]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numero_do_documento_paciente',
            field=models.CharField(error_messages={'unique': 'Número de documento já cadastrado, insira outro.'}, max_length=11, unique=True, validators=[verificacao.validator.validate_cpfrg, verificacao.validator.validate_digits]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo_paciente',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=3),
        ),
    ]