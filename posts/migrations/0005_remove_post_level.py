# Generated by Django 4.2.9 on 2024-04-12 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment_author_voice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='level',
        ),
    ]