# Generated by Django 4.2.6 on 2023-10-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_remove_image_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='result',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
