# Generated by Django 4.0.3 on 2022-03-21 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hashtag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
