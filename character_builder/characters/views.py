from characters.models.character import Character
from characters.models.event import Event
from characters.models.skill import Skill
from characters.serializer import CharacterSerializer
from characters.serializer import EventSerializer
from characters.serializer import SkillSerializer
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
    return "HIYA"
    your_characters_list = Character.objects.filter(character__user_id=request.user.id)
    context = {"your_characters_list": your_characters_list}
    return render(request, "characters/index.html", context)
