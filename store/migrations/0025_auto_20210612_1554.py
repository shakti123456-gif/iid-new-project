# Generated by Django 2.1.7 on 2021-06-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_auto_20210612_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='check',
            field=models.BooleanField(default=True),
        ),
    ]