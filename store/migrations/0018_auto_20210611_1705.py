# Generated by Django 2.1.7 on 2021-06-11 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20210611_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allorders',
            name='all1',
        ),
        migrations.RemoveField(
            model_name='allorders',
            name='user',
        ),
        migrations.DeleteModel(
            name='allorders',
        ),
    ]
