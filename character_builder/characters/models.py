from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)
    prerequisite = models.ForeignKey("self", null=True, on_delete=models.SET_NULL, blank=True)
    cost = models.IntegerField(default=2, null=True)

    def __str__(self):
        return f"{self.name}"


class Character(models.Model):
    full_name = models.CharField(max_length=200, unique=True)
    total_cp = models.IntegerField(null=True)
    skills = models.ManyToManyField(Skill, null=True, blank=True)

    @property
    def cp_spent(self):
        my_skills = Skill.objects.filter(character__id=self.id)
        cp_count = 0
        for skill in my_skills:
            cp_count += skill.cost
        return cp_count

    @property
    def cp_remaining(self):
        return self.total_cp - self.cp_spent

    def __str__(self):
        return f"{self.full_name}"


class Event(models.Model):
    title = models.TextField()
    date = models.DateTimeField()
    characters = models.ManyToManyField(Character, null=True, blank=True)
