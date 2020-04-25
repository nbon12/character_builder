from characters.models import Character
from characters.models import Event
from characters.models import Skill
from django.contrib import admin

# Register your models here.
admin.site.register(Character)
admin.site.register(Skill)
admin.site.register(Event)
