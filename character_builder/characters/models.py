from django.db import models

# Create your models here.


class Skill(models.Model):
    cost = models.IntegerField(default=2)
    description = models.TextField(null=True)
    prerequisite = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
class Subskill(models.Model):
    parent_skill = models.ForeignKey(Skill, null=False, on_delete=models.CASCADE)
class Character(models.Model):
    full_name = models.CharField(max_length=200)
    total_cp = models.IntegerField(null=True)
    skills = models.ManyToManyField(Skill)
class Event(models.Model):
    characters = models.ForeignKey(Character, null=True, on_delete=models.SET_NULL)
