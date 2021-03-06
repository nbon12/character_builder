"""character_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from characters.views import character_sheet
from characters.views import index
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("characters/", include("characters.urls"), name="characters-list"),
    path("plot/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),  # noqa E501
    path("accounts/", include("allauth.urls")),
    path("", index),
    path("character-sheet/<int:character_id>", character_sheet),
]
