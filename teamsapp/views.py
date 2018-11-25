from django.shortcuts import redirect, render, Http404
from django.utils import timezone

from .models import Team, Member


def teams(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        context = {'teams': teams}
        return render(request, 'teamsapp/teams.html', context)
    else:
        return Http404('Not allowd')

def create_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name', None)

        team = Team(name=team_name)
        team.save()

        teams = Team.objects.all()

        context = {'teams': teams}

        return render(request, 'teamsapp/teams.html', context)
    else:
        return Http404('Not allowed')

