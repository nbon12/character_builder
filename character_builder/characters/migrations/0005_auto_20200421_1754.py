# Generated by Django 3.0.5 on 2020-04-21 17:54
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("characters", "0004_auto_20200421_1739")]

    operations = [
        migrations.RemoveField(model_name="character", name="subskills"),
        migrations.AddField(
            model_name="character",
            name="skills",
            field=models.ManyToManyField(blank=True, null=True, to="characters.Skill"),
        ),
        migrations.AddField(model_name="skill", name="cost", field=models.IntegerField(default=2, null=True)),
        migrations.DeleteModel(name="Subskill"),
    ]
