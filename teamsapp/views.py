from django.shortcuts import redirect, render, Http404
from django.utils import timezone

from .models import Team, Member


def teams(request, email):
    if request.method == 'GET':
        member = Member.objects.get(email=email)
        teams = member.teams.all() 
        context = {
                'email': email,
                'teams': teams
                }
        return render(request, 'teamsapp/teams.html', context)
    else:
        return Http404('Not allowd')

def create_team(request, email):
    if request.method == 'POST':
        team_name = request.POST.get('team_name', None)

        team = Team(name=team_name)
        team.save()

        member = Member.objects.get(email=email)

        team.member_set.add(member)

        teams = member.teams.all() 

        context = {
                'email': email,
                'teams': teams
                }

        return render(request, 'teamsapp/teams.html', context)
    else:
        return Http404('Not allowed')

