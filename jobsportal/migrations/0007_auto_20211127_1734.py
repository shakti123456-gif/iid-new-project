# Generated by Django 2.1.7 on 2021-11-27 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobsportal', '0006_auto_20211125_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_apply',
            name='Experience',
            field=models.CharField(choices=[('1', '0-1'), ('2', '1-2'), ('3', '2-3')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student_apply',
            name='student_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]