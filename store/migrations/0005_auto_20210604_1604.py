# Generated by Django 2.1.7 on 2021-06-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210603_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='phone',
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
