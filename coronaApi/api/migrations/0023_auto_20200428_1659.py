# Generated by Django 3.0.5 on 2020-04-28 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20200428_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exame',
            old_name='Paciente',
            new_name='paciente',
        ),
    ]
