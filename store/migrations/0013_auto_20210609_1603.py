# Generated by Django 2.1.7 on 2021-06-09 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210609_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kingorder',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, related_name='orders', to='store.KingOrderItems'),
        ),
        migrations.AlterField(
            model_name='kingorder',
            name='ordered',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='kingorder',
            name='ordered_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kingorder',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='kingorder',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user3', to=settings.AUTH_USER_MODEL),
        ),
    ]