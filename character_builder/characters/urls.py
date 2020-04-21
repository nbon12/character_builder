from django.urls import path
from django.urls import include
from characters.views import CharacterDetailView
from characters.views import SkillDetailView

from characters import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'characters', CharacterDetailView)
router.register(r'skills', SkillDetailView)
#hi
urlpatterns = [
    path('', include(router.urls)),
    #path('', views.CharacterDetailView.as_view(), name='index'),
    #path('<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
]