from django.shortcuts import render
from .forms import PlayerForm, TeamForm
from .models import Player, Team

# Create your views here.


def playerpage(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
    players = Player.objects.all()
    form = PlayerForm()
    return render(request, "player.html", {"form": form, "players": players})


def teampage(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
    teams = Team.objects.all()
    form = TeamForm()
    return render(request, "team.html", {"form": form, "teams": teams})
