# dashboard/views.py
from django.shortcuts import render, Http404
from django.utils import timezone

from .models import Board
from teamsapp.models import Team


def dashboard(request, team_name):
    """
        Lists the boards of a given team
    """
    if request.method == 'GET':
        selected_team = Team.objects.get(name=team_name)
        boards = selected_team.board_set.all()
        context = {
                'team': selected_team,
                'boards': boards
                }
        return render(request, 'dashboard/dashboard.html', context)
    else:
        return Http404('Not allowed')


def create_board(request, team_name):
    """
        Creates a board for a team
    """
    if request.method == 'POST':
        selected_team = Team.objects.get(name=team_name)
        board_name = request.POST.get('new_board_name', None)
        slug = board_name
        
        selected_team.board_set.create(name=board_name, slug=slug)
        boards = selected_team.board_set.all()
        context = {
                'team': selected_team,
                'boards': boards
                }
        
        return render(request, 'dashboard/dashboard.html', context)
    else:
        return Http404('Not allowed')


def board(request, team_name, board_name):
    """
        Shows a board, its columns ands tasks
    """
    if request.method == 'GET':
        selected_team = Team.objects.get(name=team_name)
        selected_board = selected_team.board_set.get(name=board_name)
        columns = selected_board.column_set.order_by('index')
        context = {
            'team': selected_team,
            'board': selected_board,
            'columns': columns
            }
        return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not allowed')


def delete_board(request, team_name, board_name):
    """
        Deletes a selected board, validates it it doesn't have columns
    """
    if request.method == 'POST':
        selected_team = Team.objects.get(name=team_name)
        selected_board = selected_team.board_set.get(name=board_name)
        if len(selected_board.column_set.all()) < 1:
            selected_board.delete()
            boards = Board.objects.all()
            message = "Board deleted successfully"
            context = {
                    'message': message,
                    'team': selected_team,
                    'boards': boards
                    }

            return render(request, 'dashboard/dashboard.html', context) 
        else:
            message = "The board still has columns, it can not be deleted"
            columns = selected_board.column_set.all()

            context = {
                    'message': message,
                    'team': selected_team,
                    'board': selected_board,
                    'columns': columns
                    }
            return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not Allowed')


def create_column(request, team_name, board_name):
    """
        Creates a column inside the board
    """
    if request.method == 'POST':
        selected_team = Team.objects.get(name=team_name)
        selected_board = selected_team.board_set.get(name=board_name)
        column_name = request.POST.get('new_column_name', None)
        column_index = len(selected_board.column_set.all())
        selected_board.column_set.create(name=column_name, index=column_index)

        columns = selected_board.column_set.all()

        context = {
                'team': selected_team,
                'board': selected_board,
                'columns': columns
                }
        return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not allowed')


def delete_column(request, team_name, board_name):
    """
        Deletes a column of the given board, validates if it doesn't have tasks
    """
    if request.method == 'POST':
        selected_team = Team.objects.get(name=team_name)
        selected_board = selected_team.board_set.get(name=board_name)
        selected_column = selected_board.column_set.get(name=request.POST.get('column_name', None))
        if len(selected_column.task_set.all()) < 1:
            selected_column.delete()

            columns = selected_board.column_set.all()
            context = {
                    'team': selected_team,
                    'board': selected_board,
                    'columns': columns
                    }
            return render(request, 'dashboard/board.html', context)
        else:
            message = "The column still has tasks, it can not be deleted"
            columns = selected_board.column_set.all()

            context = {
                    'team': selected_team,
                    'board': selected_board,
                    'message': message,
                    'columns': columns
                    }
            return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not allowed')


def create_task(request, team_name, board_name):
    """
        Creates a task inside a column
    """
    if request.method == 'POST':
        selected_team = Team.objects.get(name=team_name)
        selected_board = selected_team.board_set.get(name=board_name)
        selected_column = selected_board.column_set.get(name=request.POST.get('column_name', None))
        task_title = request.POST.get('title', None)
        task_description = request.POST.get('description', None)
        
        selected_column.task_set.create(title=task_title, description=task_description, creation_date = timezone.now())

        columns = selected_board.column_set.all()
        
        context = {
                'team': selected_team,
                'board': selected_board,
                'columns': columns
                }
        return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not allowed')


def delete_task(request, team_name, board_name):
    """
        Deletes a task
    """
    if request.method == 'POST':
        selected_team = Team.objects.get(name=team_name)
        selected_board = selected_team.board_set.get(name=board_name)
        selected_column = selected_board.column_set.get(name=request.POST.get('column_name', None))
        selected_task = selected_column.task_set.get(title=request.POST.get('task_title', None))
        
        selected_task.delete()
        
        columns = selected_board.column_set.all()

        context = {
                'team': selected_team,
                'board': selected_board,
                'columns': columns
                }

        return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not allowed')

