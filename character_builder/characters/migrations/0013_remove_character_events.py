# Generated by Django 3.0.5 on 2020-04-25 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0012_auto_20200425_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='events',
        ),
    ]
