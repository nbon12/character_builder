from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.detail import DetailView
from rest_framework.generics import GenericAPIView
from characters.serializer import CharacterSerializer
from characters.serializer import SkillSerializer
from characters.models import Skill
from rest_framework import viewsets

from characters.models import Character

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



    