# Generated by Django 2.1.7 on 2021-06-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_billingaddress_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='appartment_address',
        ),
        migrations.RemoveField(
            model_name='billingaddress',
            name='country',
        ),
        migrations.RemoveField(
            model_name='billingaddress',
            name='street_address',
        ),
        migrations.RemoveField(
            model_name='billingaddress',
            name='zip',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='address_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='address_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='check',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='zip_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]