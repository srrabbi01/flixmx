# Generated by Django 3.2 on 2021-08-15 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210808_0008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seasonmodel',
            options={'ordering': ('series__title', 'season_number')},
        ),
    ]
