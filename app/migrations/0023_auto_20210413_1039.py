# Generated by Django 2.1.7 on 2021-04-13 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20210223_1833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webinar',
            options={'verbose_name': 'Webinar', 'verbose_name_plural': 'Webinars'},
        ),
        migrations.AlterField(
            model_name='pilotlist',
            name='certificate_no',
            field=models.CharField(max_length=40, verbose_name='Certificate Number'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='description1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Speaker 1'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='description2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Speaker 2'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='description3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Speaker 3'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='description4',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Speaker 4'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='description5',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Speaker 5'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='registration_url',
            field=models.URLField(verbose_name='Registration Link'),
        ),
        migrations.AlterField(
            model_name='webinar',
            name='topic',
            field=models.CharField(max_length=100, verbose_name='Topic'),
        ),
    ]
