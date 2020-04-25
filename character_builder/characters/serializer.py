"""Serializers for the Django Rest Framework."""
from characters.models import Character
from characters.models import Event
from characters.models import Skill
from rest_framework import serializers


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ["full_name", "total_cp", "skills", "cp_spent", "cp_remaining"]


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ["name", "description", "prerequisite", "cost"]


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "date", "characters"]
