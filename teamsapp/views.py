from django.shortcuts import render, Http404

from .models import Team, Member


def teams(request, email):
    if request.method == 'GET':
        member = Member.objects.get(email=email)
        member_teams = member.teams.all() 
        all_teams = Team.objects.all()
        context = {
                'email': email,
                'member_teams': member_teams,
                'all_teams': all_teams
                }
        return render(request, 'teamsapp/teams.html', context)
    else:
        return Http404('Not allowed')


def update_member_teams(request, email):
    if request.method == 'POST':
        member = Member.objects.get(email=email)
        all_teams = Team.objects.all()

        for team in all_teams:
            if request.POST.get(team.name, None):
                member.teams.add(team)
        
        member_teams = member.teams.all()
       
        context = {
                'email': email,
                'member_teams': member_teams,
                'all_teams': all_teams
                }

        return render(request, 'teamsapp/teams.html', context)
    else:
        return Http404('Not allowed')


def create_team(request, email):
    if request.method == 'POST':
        team_name = request.POST.get('team_name', None)

        team = Team(name=team_name)
        team.save()

        member = Member.objects.get(email=email)

        team.member_set.add(member)

        member_teams = member.teams.all()
        all_teams = Team.objects.all()

        context = {
                'email': email,
                'member_teams': member_teams,
                'all_teams': all_teams
                }

        return render(request, 'teamsapp/teams.html', context)
    else:
        return Http404('Not allowed')

