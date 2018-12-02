# dashboard/views.py
from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages
from django.utils import timezone
from django.utils.text import slugify

from .models import Board
from teamsapp.models import Team


def dashboard(request, team_name):
    """
        Lists the boards of a given team
    """
    if request.method == 'GET':
        email = request.session.get('email', None)
        full_name = request.session.get('full_name', None)
        selected_team = Team.objects.get(name=team_name)
        boards = selected_team.board_set.all()
        context = {
                'email': email,
                'full_name': full_name,
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
        slug = slugify(board_name)
        selected_team.board_set.create(name=board_name, slug=slug)

        message = "Board created successfully"
        messages.add_message(request, messages.INFO, message)
        return redirect('dashboard:dashboard', team_name=team_name)
    else:
        return Http404('Not allowed')


def board(request, team_name, board_name):
    """
        Shows a board, its columns ands tasks
    """
    if request.method == 'GET':
        email = request.session.get('email', None)
        full_name = request.session.get('full_name', None)
        selected_team = Team.objects.get(name=team_name)
        selected_board = selected_team.board_set.get(name=board_name)
        columns = selected_board.column_set.order_by('index')
        context = {
            'email': email,
            'full_name': full_name,
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
        if selected_board.column_set.count() < 1:
            selected_board.delete()

            message = "Board deleted successfully"
            messages.add_message(request, messages.INFO, message)
            return redirect('dashboard:dashboard', team_name=team_name)
        else:
            message = "The board still has columns, it can not be deleted"
            messages.add_message(request, messages.INFO, message)
            return redirect('dashboard:board', team_name=team_name, board_name=board_name)
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
        column_index = selected_board.column_set.count()
        selected_board.column_set.create(name=column_name, index=column_index)

        message = "Column created successfully"
        messages.add_message(request, messages.INFO, message)
        return redirect('dashboard:board', team_name=team_name, board_name=board_name)
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
        if selected_column.task_set.count() < 1:
            selected_column.delete()

            message = "Column deleted successfully"
            messages.add_message(request, messages.INFO, message)
            return redirect('dashboard:board', team_name=team_name, board_name=board_name)
        else:
            message = "The column still has tasks, it can not be deleted"
            messages.add_message(request, messages.INFO, message)
            return redirect('dashboard:board', team_name=team_name, board_name=board_name)
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

        message = "Task created successfully"
        messages.add_message(request, messages.INFO, message)
        return redirect('dashboard:board', team_name=team_name, board_name=board_name)
    else:
        return Http404('Not allowed')


def move_task_right(request, team_name, board_name):
    """
        Moves the task to the next column to the right
    """
    if request.method == 'POST':
        selected_team = Team.objects.get(name=team_name)
        selected_board = selected_team.board_set.get(name=board_name)
        selected_column = selected_board.column_set.get(name=request.POST.get('column_name', None))
        selected_task = selected_column.task_set.get(title=request.POST.get('task_title', None))
        current_index = selected_column.index

        if not current_index == selected_board.column_set.count()-1:
            selected_board.column_set.get(index=current_index+1).task_set.add(selected_task)
            message = "Task moved successfully"
        else:
            message = "There is not columns to the right, the task can't be moved"

        messages.add_message(request, messages.INFO, message)
        return redirect('dashboard:board', team_name=team_name, board_name=board_name)
    else:
        return Http404('Not allowed')


def move_task_left(request, team_name, board_name):
    """
        Moves the task to the next column to the left
    """
    if request.method == 'POST':
        selected_team = Team.objects.get(name=team_name)
        selected_board = selected_team.board_set.get(name=board_name)
        selected_column = selected_board.column_set.get(name=request.POST.get('column_name', None))
        selected_task = selected_column.task_set.get(title=request.POST.get('task_title', None))
        current_index = selected_column.index

        if not current_index == 0:
            selected_board.column_set.get(index=current_index-1).task_set.add(selected_task)
            message = "Task moved successfully"
        else:
            message = "There is not columns to the left, the task can't be moved"

        messages.add_message(request, messages.INFO, message)
        return redirect('dashboard:board', team_name=team_name, board_name=board_name)
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
        
        message = "Task deleted successfully"
        messages.add_message(request, messages.INFO, message)
        return redirect('dashboard:board', team_name=team_name, board_name=board_name)
    else:
        return Http404('Not allowed')

