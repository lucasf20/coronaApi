# Generated by Django 3.0.5 on 2020-04-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20200428_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='radiografia',
        ),
        migrations.AlterField(
            model_name='exame',
            name='radiografia',
            field=models.TextField(),
        ),
    ]
