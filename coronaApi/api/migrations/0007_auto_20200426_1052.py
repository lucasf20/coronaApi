# Generated by Django 3.0.5 on 2020-04-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200426_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='covid',
            field=models.IntegerField(default=-1, editable=False),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='gripe_comum',
            field=models.IntegerField(default=-1, editable=False),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='h1n1',
            field=models.IntegerField(default=-1, editable=False),
        ),
    ]
