# Generated by Django 2.1.7 on 2021-06-11 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20210611_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kingorder',
            options={'verbose_name': 'ProductsOrder'},
        ),
        migrations.AlterField(
            model_name='kingorder',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]