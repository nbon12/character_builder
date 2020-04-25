from characters.views import CharacterDetailView
from characters.views import EventView
from characters.views import SkillDetailView
from django.urls import include
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"characters", CharacterDetailView)
router.register(r"skills", SkillDetailView)
router.register(r"events", EventView)

urlpatterns = [path("", include(router.urls))]
