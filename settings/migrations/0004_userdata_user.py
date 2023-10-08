# Generated by Django 4.2.6 on 2023-10-08 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0003_remove_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
