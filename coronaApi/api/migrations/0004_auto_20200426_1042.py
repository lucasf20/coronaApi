# Generated by Django 3.0.5 on 2020-04-26 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200426_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='covid',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='gripe_comum',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='h1n1',
        ),
    ]
