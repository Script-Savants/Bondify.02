# Generated by Django 5.0.7 on 2024-07-10 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
    ]
