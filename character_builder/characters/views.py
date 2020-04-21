from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.detail import DetailView
from rest_framework.generics import GenericAPIView
from characters.serializer import CharacterSerializer
from rest_framework import viewsets

from characters.models import Character

class CharacterDetailView(viewsets.ModelViewSet):

    model = Character
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
    lookup_field = 'full_name'
    # def get_context_data(self, **kwargs):
    #      context = super().get_context_data(**kwargs)
    #      context['now'] = timezone.now()
    #      return context

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the Characters index")

    