# Generated by Django 2.1.7 on 2020-12-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20201202_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='CoverImage',
            field=models.ImageField(blank=True, upload_to='Blog/CoverImage/'),
        ),
        migrations.AlterField(
            model_name='author',
            name='Img',
            field=models.ImageField(upload_to='Blog/AuthorImage/'),
        ),
    ]