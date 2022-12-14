# Generated by Django 4.1.1 on 2022-10-25 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_paciente', models.CharField(max_length=256)),
                ('sexo_paciente', models.CharField(max_length=1)),
                ('data_nascimento_paciente', models.DateField()),
                ('municipio_paciente', models.CharField(max_length=256)),
                ('cep_paciente', models.CharField(max_length=8)),
                ('endereco_paciente', models.CharField(max_length=256)),
                ('bairro_paciente', models.CharField(max_length=256)),
                ('numero_paciente', models.IntegerField()),
                ('estado_paciente', models.CharField(max_length=10)),
                ('cartao_sus_paciente', models.CharField(max_length=15)),
                ('documento_paciente', models.CharField(max_length=256)),
                ('numero_do_documento_paciente', models.CharField(max_length=11)),
                ('contato_emergencia_paciente', models.CharField(max_length=11)),
            ],
        ),
    ]
