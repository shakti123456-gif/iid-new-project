# Generated by Django 2.1.7 on 2021-11-30 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsportal', '0008_auto_20211130_1052'),
        ('account', '0005_auto_20211114_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermembership',
            name='membership_method',
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='usermembership',
        ),
        migrations.DeleteModel(
            name='membership',
        ),
        migrations.DeleteModel(
            name='UserMembership',
        ),
    ]