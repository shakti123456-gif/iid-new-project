# Generated by Django 2.1.7 on 2021-01-09 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210109_1542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iidlocations',
            options={'verbose_name': 'IID Location', 'verbose_name_plural': 'IID Locations'},
        ),
        migrations.AlterModelOptions(
            name='trainingschedule',
            options={'verbose_name': 'Training Schedule', 'verbose_name_plural': 'Training Schedule'},
        ),
    ]
