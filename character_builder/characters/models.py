from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)
    prerequisite = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
class Subskill(models.Model):
    parent_skill = models.ForeignKey(Skill, null=False, on_delete=models.CASCADE)
    cost = models.IntegerField(default=2, null=True)
class Character(models.Model):
    full_name = models.CharField(max_length=200)
    total_cp = models.IntegerField(null=True)
    subskills = models.ManyToManyField(Subskill, null=True, blank=True)
class Event(models.Model):
    characters = models.ForeignKey(Character, null=True, on_delete=models.SET_NULL)
