# Generated by Django 2.1.7 on 2021-06-03 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210602_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='email',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]