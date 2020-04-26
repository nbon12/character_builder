from characters.models.character import Character
from characters.models.event import Event
from characters.models.skill import Skill
from django.contrib import admin

# Register your models here.
admin.site.register(Character)
admin.site.register(Skill)
admin.site.register(Event)
admin.site.site_header = "Character Builder Administration"
admin.site.site_title = "Character Builder Administration"
admin.site.index_title = "Admin Character Builder"
# admin.site.register()
