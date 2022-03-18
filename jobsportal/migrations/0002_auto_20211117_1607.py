# Generated by Django 2.1.7 on 2021-11-17 10:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20211114_1858'),
        ('jobsportal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.RemoveField(
            model_name='job',
            name='company',
        ),
        migrations.RemoveField(
            model_name='job',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='job',
            name='image',
        ),
        migrations.RemoveField(
            model_name='job',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='job',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='job',
            name='start_date',
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='job',
            name='filled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='last_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='type',
            field=models.CharField(blank=True, choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.UserMembership'),
        ),
        migrations.AddField(
            model_name='job',
            name='website',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
