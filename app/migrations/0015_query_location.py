# Generated by Django 2.1.7 on 2021-01-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210115_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='Location',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='First Name'),
        ),
    ]
