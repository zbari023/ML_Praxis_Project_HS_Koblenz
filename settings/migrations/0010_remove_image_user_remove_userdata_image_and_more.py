# Generated by Django 4.2.6 on 2023-10-16 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_alter_image_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='image',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='user',
        ),
    ]
