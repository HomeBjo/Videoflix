# Generated by Django 5.0.7 on 2024-07-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Video_App', '0006_alter_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='favorite',
        ),
        migrations.AddField(
            model_name='favoritevideo',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]