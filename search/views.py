# search/views.py
from django.shortcuts import render, Http404
from django.http import JsonResponse

from dashboard.models import Board
from teamsapp.models import Team
from welcome.views import session_required


@session_required
def search_team_boards(request):
    """
        Search boards on a team given a search pattern
    """
    if request.method == 'GET':
        search_pattern = request.GET.get('search_pattern', None)
        team_name = request.GET.get('team_name', None)
        selected_team = Team.objects.get(name=team_name)
        boards = selected_team.board_set.filter(slug__icontains=search_pattern)
        items = [] 
        for board in boards:
            dict = {'board_name': board.name}
            items.append(dict)
            data = {
                'boards': items
                }
        return JsonResponse(data)
    else:
        raise Http404('Not allowed')


@session_required
def search_teams(request):
    """
        Search any team given a search_pattern
    """
    if request.method == 'GET':
        search_pattern = request.GET.get('search_pattern', None)
        teams = Team.objects.filter(name__icontains=search_pattern)
        items = []
        for team in teams:
            dict = {'team_name': team.name}
            items.append(dict)
        data = {
            'teams': items
            }
        return JsonResponse(data)
    else:
        raise Http404('Not allowed')
