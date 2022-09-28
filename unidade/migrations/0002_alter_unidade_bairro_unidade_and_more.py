# Generated by Django 4.1.1 on 2022-09-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unidade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidade',
            name='bairro_unidade',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='cep_unidade',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='cnes',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='cnpj',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='endereco_unidade',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='estado_unidade',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='nome_unidade',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='numero_unidade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='orgaoEmissor_unidade',
            field=models.CharField(max_length=256),
        ),
    ]