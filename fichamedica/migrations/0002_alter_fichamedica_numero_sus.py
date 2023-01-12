# Generated by Django 4.1.1 on 2023-01-12 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_remove_paciente_id_and_more'),
        ('fichamedica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichamedica',
            name='Numero_SUS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SUS', to='paciente.paciente'),
        ),
    ]
