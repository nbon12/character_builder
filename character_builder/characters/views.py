from characters.models import Character
from characters.models import Event
from characters.models import Skill
from characters.serializer import CharacterSerializer
from characters.serializer import EventSerializer
from characters.serializer import SkillSerializer
from django.http import HttpResponse
from rest_framework import viewsets


class CharacterDetailView(viewsets.ModelViewSet):

    model = Character
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the Characters index")


class SkillDetailView(viewsets.ModelViewSet):
    model = Skill
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class EventView(viewsets.ModelViewSet):
    model = Event
    serializer_class = EventSerializer
    queryset = Event.objects.all()
