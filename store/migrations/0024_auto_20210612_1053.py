# Generated by Django 2.1.7 on 2021-06-12 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20210612_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kingorder',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='kingorder',
            name='shipment',
            field=models.CharField(blank=True, choices=[('Processing', 'Processing'), ('Completed', 'Completed'), ('Active', 'Active')], default='Active', max_length=100, null=True),
        ),
    ]
