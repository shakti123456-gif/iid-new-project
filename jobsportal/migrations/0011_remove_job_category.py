# Generated by Django 2.1.7 on 2021-11-30 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsportal', '0010_auto_20211130_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='category',
        ),
    ]
