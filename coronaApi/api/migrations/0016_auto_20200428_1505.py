# Generated by Django 3.0.5 on 2020-04-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20200428_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exame',
            name='id_exame',
        ),
        migrations.AddField(
            model_name='exame',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
