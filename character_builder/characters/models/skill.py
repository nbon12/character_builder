from django.db import models

# from characters.models.event import Event

# Create your models here.


class Skill(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)
    prerequisite = models.ForeignKey("self", null=True, on_delete=models.SET_NULL, blank=True)
    cost = models.IntegerField(default=2, null=True)

    @property
    def child_skills(self):
        """A list of all the skills that require this skill as a prerequisite."""
        child_skills = Skill.objects.filter(prerequisite=self)
        return child_skills

    def __str__(self):
        return f"{self.name}"
