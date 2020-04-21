"""Serializers for the Django Rest Framework."""
from characters.models import Character
from characters.models import Skill
from characters.models import Subskill
from rest_framework import serializers

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ['full_name', 'total_cp', 'skills']

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ['cost', 'description', 'prerequisite']

class SubskillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subskill
        fields = ['parent_skill']