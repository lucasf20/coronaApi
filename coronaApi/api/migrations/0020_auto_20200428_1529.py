# Generated by Django 3.0.5 on 2020-04-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_exame_radiografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='nome_doenca',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='observacao',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
