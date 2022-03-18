# Generated by Django 2.1.7 on 2021-01-08 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201012_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('url1', models.URLField(default='')),
                ('Address', models.TextField()),
                ('Phone1', models.CharField(max_length=12)),
                ('Phone2', models.CharField(max_length=12)),
                ('email1', models.EmailField(blank=True, default='', max_length=254, null=True)),
                ('email2', models.EmailField(default='', max_length=254)),
                ('type', models.CharField(choices=[('head_office', 'head_office'), ('Partners', 'Partners'), ('Franchisee', 'Franchisee')], default='not me', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Traning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.contactinfo')),
                ('coursename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Item')),
            ],
        ),
    ]