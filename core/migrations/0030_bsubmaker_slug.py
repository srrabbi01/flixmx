# Generated by Django 3.2.9 on 2022-02-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20220219_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='bsubmaker',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
