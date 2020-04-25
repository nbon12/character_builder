"""Serializers for the Django Rest Framework."""
from characters.models import Character
from characters.models import Skill
from rest_framework import serializers


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    # cp_spent = serializers.SerializerMethodField('get_cp_spent')
    # cp_remaining = serializers.SerializerMethodField('get_cp_remaining')

    # def get_cp_spent(self, obj):
    #     my_skills = Skill.objects.filter(character__id=obj.id)
    #     cp_count = 0
    #     for skill in my_skills:
    #         cp_count += skill.cost
    #         cp_remaining = cp_count - obj.total_cp
    #     return cp_count

    # def get_cp_remaining(self, obj):
    #     print('when calculating remaining, spent is..')
    #     print(obj.__repr__()
    #     return 5
    class Meta:
        model = Character
        fields = ["full_name", "total_cp", "skills", "cp_spent", "cp_remaining"]


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ["name", "description", "prerequisite", "cost"]
