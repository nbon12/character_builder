# Generated by Django 3.0.5 on 2020-04-25 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_remove_event_characters'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='events',
            field=models.ManyToManyField(blank=True, to='characters.Event'),
        ),
    ]
