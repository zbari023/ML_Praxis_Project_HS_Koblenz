# Generated by Django 4.2.6 on 2023-10-20 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0012_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='result',
        ),
    ]