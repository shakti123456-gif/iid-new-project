# Generated by Django 2.1.7 on 2021-11-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20210629_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='timezone',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]