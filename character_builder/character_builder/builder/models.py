from django.db import models

class Character(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name
    
class Event(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name + ' on ' + date
    