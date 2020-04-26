from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# from characters.models.event import Event

# Create your models here.


class Skill(MPTTModel):
    name = models.TextField()
    description = models.TextField(null=True)
    parent = TreeForeignKey("self", null=True, on_delete=models.SET_NULL, blank=True, related_name="children")
    cost = models.IntegerField(default=2, null=True)

    def __str__(self):
        return f"{self.name}"
