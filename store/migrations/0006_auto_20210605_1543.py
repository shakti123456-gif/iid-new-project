# Generated by Django 2.1.7 on 2021-06-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210604_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='description1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
