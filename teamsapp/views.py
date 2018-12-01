# teamsapp/views.py
from django.shortcuts import render, redirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from .models import Team, Member


def teams(request, email, full_name):
    """
        Lists the member teams.
    """
    if request.method == 'GET':
        # Validates if the member exists. If members logon successfully they are created on the teams-app.
        try: 
            member = Member.objects.get(email=email)
        except ObjectDoesNotExist:
            member = Member(email=email, full_name=full_name)
            member.save()

        member_teams = member.teams.all() 
        context = {
            'email': email,
            'full_name': full_name,
            'member_teams': member_teams
            }
        return render(request, 'teamsapp/teams.html', context)
    else:
        raise Http404('Not allowed')


def update_member_teams(request, email, team_name):
    """
        Adds a selected team to the member teams list.
    """
    if request.method == 'GET':
        member = Member.objects.get(email=email)
        all_teams = Team.objects.all()

        for team in all_teams:
            if team.name == team_name:
                member.teams.add(team)
                break

        message = 'Member teams updated succesffully'
        messages.add_message(request, messages.INFO, message)
        return redirect('teamsapp:teams', email=email, full_name=member.full_name)
    else:
        raise Http404('Not allowed')


def create_team(request, email):
    """
        Creates a team. It doesn't relates member and teams, so users have to use the really cool search feature.
    """
    if request.method == 'POST':
        team_name = request.POST.get('team_name', None)
        team = Team(name=team_name)
        team.save()

        member = Member.objects.get(email=email)

        message = "Team created, please use the cool search feature and assign yourself to the team"
        messages.add_message(request, messages.INFO, message)
        return redirect('teamsapp:teams', email=email, full_name=member.full_name)
    else:
        raise Http404('Not allowed')

