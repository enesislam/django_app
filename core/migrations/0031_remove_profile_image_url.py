# Generated by Django 4.0.3 on 2022-03-30 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_profile_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image_url',
        ),
    ]
