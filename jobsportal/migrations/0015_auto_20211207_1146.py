# Generated by Django 2.1.7 on 2021-12-07 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsportal', '0014_auto_20211207_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcategory',
            name='description1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='allcategory',
            name='description2',
            field=models.CharField(default='', max_length=200),
        ),
    ]