# Generated by Django 2.1.7 on 2020-12-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_auto_20201205_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Date',
            field=models.DateField(blank=True),
        ),
    ]
