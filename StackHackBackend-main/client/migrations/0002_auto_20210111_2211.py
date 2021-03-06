# Generated by Django 3.1.3 on 2021-01-11 16:41

import client.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='preview_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to=client.models.content_file_name),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]
