# Generated by Django 4.0.3 on 2022-03-23 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_profile_is_online'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='hashtag_name',
            new_name='name',
        ),
    ]
