from characters.models.character import Character
from characters.models.event import Event
from characters.models.skill import Skill
from characters.serializer import CharacterSerializer
from characters.serializer import EventSerializer
from characters.serializer import SkillSerializer
from django.template.loader import render_to_string
from django.shortcuts import render
from rest_framework import viewsets


class CharacterDetailView(viewsets.ModelViewSet):

    model = Character
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


class SkillDetailView(viewsets.ModelViewSet):
    model = Skill
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class EventView(viewsets.ModelViewSet):
    model = Event
    serializer_class = EventSerializer
    queryset = Event.objects.all()


def index(request):
    your_characters_list = Character.objects.filter(user_id=request.user.id)
    context = {"your_characters_list": your_characters_list}
    return render(request, "characters/index.html", context)


def character_sheet(request, character_id):
    character = Character.objects.filter(id=character_id)[0]
    parent_skills = Skill.objects.filter(prerequisite=None)
    my_skills = Skill.objects.filter(character=character)
    context = {"character": character, "skills": parent_skills, "my_skills": my_skills}
    return render(request, "characters/character-sheet.html", context)
