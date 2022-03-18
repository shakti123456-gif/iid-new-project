# Generated by Django 2.1.7 on 2021-01-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_check'),
    ]

    operations = [
        migrations.DeleteModel(
            name='check',
        ),
        migrations.AlterField(
            model_name='iidlocations',
            name='Phone2',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='iidlocations',
            name='email1',
            field=models.EmailField(default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='iidlocations',
            name='email2',
            field=models.EmailField(blank=True, default='', max_length=254, null=True),
        ),
    ]