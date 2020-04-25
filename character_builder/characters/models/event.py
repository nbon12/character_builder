from django.db import models


class Event(models.Model):
    title = models.TextField()
    date = models.DateField()
    characters = models.ManyToManyField("Character", blank=True)

    @property
    def year_month(self):
        return f"{self.date.month}" + "/" + f"{self.date.day}" + "/" + f"{self.date.year}"

    def __str__(self):
        return f"{self.date}"
