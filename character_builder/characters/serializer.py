"""Serializers for the Django Rest Framework."""
from characters.models.character import Character
from characters.models.event import Event
from characters.models.skill import Skill
from rest_framework import serializers


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ["full_name", "starting_cp", "skills", "cp_spent", "cp_remaining", "events_attended"]


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ["name", "description", "prerequisite", "cost"]


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "date", "characters"]
