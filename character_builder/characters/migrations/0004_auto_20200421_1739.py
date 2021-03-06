# Generated by Django 3.0.5 on 2020-04-21 17:39
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("characters", "0003_skill_name")]

    operations = [
        migrations.AddField(
            model_name="event",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="event", name="title", field=models.TextField(default="Welcome to LOE"), preserve_default=False
        ),
        migrations.AlterField(
            model_name="subskill",
            name="parent_skill",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="subskills", to="characters.Skill"
            ),
        ),
    ]
