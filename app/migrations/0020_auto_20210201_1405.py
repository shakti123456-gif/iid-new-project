# Generated by Django 2.1.7 on 2021-02-01 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20210201_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='webniar',
            name='description1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='webniar',
            name='description2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='webniar',
            name='description3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='webniar',
            name='description4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='webniar',
            name='description5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]