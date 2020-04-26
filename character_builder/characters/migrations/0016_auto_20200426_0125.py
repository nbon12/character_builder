# Generated by Django 3.0.5 on 2020-04-26 01:25
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL), ("characters", "0015_character_user")]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="user",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        )
    ]