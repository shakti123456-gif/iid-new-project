# Generated by Django 2.1.7 on 2021-01-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210115_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='test_link',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Test Link'),
        ),
        migrations.AddField(
            model_name='item',
            name='text_book',
            field=models.FileField(blank=True, null=True, upload_to='Text Book/', verbose_name='Text Book'),
        ),
    ]