# Generated by Django 4.2.6 on 2023-10-08 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_remove_userdata_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='phone',
            field=models.CharField(max_length=40),
        ),
    ]
