# Generated by Django 4.2.9 on 2024-05-03 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_voice_info_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='recent_image_number',
            field=models.IntegerField(default=0),
        ),
    ]