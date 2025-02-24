# Generated by Django 3.2.9 on 2022-02-06 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0019_auto_20220202_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodemodel',
            name='tmdb_thumbnail',
            field=models.URLField(blank=True, max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='seriesmodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_user_series', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='seriesmodel',
            name='last_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_user_series', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='softwaresgamesmodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_user_sge', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='softwaresgamesmodel',
            name='last_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_user_sge', to=settings.AUTH_USER_MODEL),
        ),
    ]
