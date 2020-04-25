from django.db import models
from characters.models.event import Event
from characters.models.skill import Skill


class Character(models.Model):
    full_name = models.CharField(max_length=200, unique=True)
    starting_cp = models.IntegerField(null=True)
    skills = models.ManyToManyField(Skill, blank=True)

    @property
    def cp_spent(self):
        my_skills = Skill.objects.filter(character__id=self.id)
        cp_count = 0
        for skill in my_skills:
            cp_count += skill.cost
        return cp_count

    @property
    def cp_remaining(self):
        return self.starting_cp - self.cp_spent + self.events_attended

    @property
    def events_attended(self):
        events_attended = Event.objects.filter(characters__id=self.id).count()
        return events_attended

    def __str__(self):
        return f"{self.full_name}"
