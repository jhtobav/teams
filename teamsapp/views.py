from django.shortcuts import render, Http404

from .models import Team, Member


def teams(request, email):
    if request.method == 'GET':
        member = Member.objects.get(email=email)
        member_teams = member.teams.all() 
        context = {
                'email': email,
                'member_teams': member_teams,
                }
        return render(request, 'teamsapp/teams.html', context)
    else:
        raise Http404('Not allowed')


def update_member_teams(request, email, team_name):
    if request.method == 'GET':
        member = Member.objects.get(email=email)
        all_teams = Team.objects.all()

        for team in all_teams:
            if team.name == team_name:
                member.teams.add(team)
                break
        
        member_teams = member.teams.all()
       
        context = {
                'email': email,
                'member_teams': member_teams,
                }

        return render(request, 'teamsapp/teams.html', context)
    else:
        raise Http404('Not allowed')


def create_team(request, email):
    if request.method == 'POST':
        team_name = request.POST.get('team_name', None)

        team = Team(name=team_name)
        team.save()

        member = Member.objects.get(email=email)
        member_teams = member.teams.all()

        message = "Team created, please use the search feature and asign yourself to the team"
        context = {
                'message': message,
                'email': email,
                'member_teams': member_teams,
                }

        return render(request, 'teamsapp/teams.html', context)
    else:
        raise Http404('Not allowed')

