# Generated by Django 4.0.3 on 2022-03-23 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_post_hashtag_hashtag_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hashtags', to='core.post'),
        ),
    ]
