# Generated by Django 2.1.7 on 2021-06-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210611_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kingorder',
            name='shipment',
            field=models.CharField(blank=True, choices=[('Processing', 'Processing'), ('completed', 'completed'), ('Active', 'active')], default='active', max_length=100, null=True),
        ),
    ]
