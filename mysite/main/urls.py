from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("players", views.playerpage, name="playerpage"),
    path("teams", views.teampage, name="teampage"),
]
