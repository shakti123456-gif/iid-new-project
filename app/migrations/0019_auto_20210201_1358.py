# Generated by Django 2.1.7 on 2021-02-01 08:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20210201_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webniar',
            name='tentative_speakers',
        ),
        migrations.AddField(
            model_name='webniar',
            name='tentative_speakerst',
            field=ckeditor.fields.RichTextField(blank=True, default='Main Blog Content', null=True),
        ),
    ]
