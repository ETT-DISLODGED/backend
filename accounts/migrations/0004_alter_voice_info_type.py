# Generated by Django 4.2.9 on 2024-03-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_voice_info_pitch_alter_voice_info_speed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voice_info',
            name='type',
            field=models.TextField(default='ko-KR-Wavenet-A'),
        ),
    ]