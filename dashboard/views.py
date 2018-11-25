
from django.shortcuts import redirect, render, Http404
from django.utils import timezone

from .models import Board, Column, Task


def dashboard(request):
    if request.method == 'GET':
        boards = Board.objects.all()
        context = {'boards': boards}
        return render(request, 'dashboard/dashboard.html', context)
    elif request.method == 'POST':
        board_name = request.POST.get('name', None)
        slug = board_name
        creation_date = timezone.now()
        Board.objects.all().create(name=board_name, slug=slug, creation_date=creation_date)
        boards = Board.objects.all()
        context = {'boards': boards}
        return render(request, 'dashboard/dashboard.html', context)
    else:
        return Http404('Not allowed')


def board(request, board_name):
    if request.method == 'GET':
        selected_board = Board.objects.get(name=board_name)
        columns = selected_board.column_set.all()
        context = {
            'board': selected_board,
            'columns': columns,
            }
        return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not allowed')


def delete_board(request, board_name):
    if request.method == 'POST':
        selected_board = Board.objects.get(name=board_name)
        if len(selected_board.column_set.all()) < 1:
            selected_board.delete()
            boards = Board.objects.all()
            message = "Board deleted successfully"
            context = {
                    'message': message,
                    'boards': boards
                    }

            return render(request, 'dashboard/dashboard.html', context) 
        else:
            message = "The board still has columns, it can not be deleted"
            columns = selected_board.column_set.all()

            context = {
                    'message': message,
                    'board': selected_board,
                    'columns': columns
                    }
            return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not Allowed')


def create_column(request, board_name):
    if request.method == 'POST':
        selected_board = Board.objects.get(name=board_name)
        column_name = request.POST.get('new_column_name', None)
        column_index = request.POST.get('new_column_index', None)
        
        selected_board.column_set.create(name=column_name, index=column_index)

        columns = selected_board.column_set.all()

        context = {
                'board': selected_board,
                'columns': columns,
                }
        return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not allowed')

def delete_column(request, board_name):
    if request.method == 'POST':
        selected_board = Board.objects.get(name=board_name)
        selected_column = selected_board.column_set.get(name=request.POST.get('column_name', None))
        if len(selected_column.task_set.all()) < 1:
            selected_column.delete()

            columns = selected_board.column_set.all()
            context = {
                    'board': selected_board,
                    'columns': columns,
                    }
            return render(request, 'dashboard/board.html', context)
        else:
            message = "The column still has tasks, it can not be deleted"
            columns = selected_board.column_set.all()

            context = {
                    'board' : selected_board,
                    'message': message,
                    'columns': columns
                    }
            return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not allowed')


def create_task(request, board_name):
    if request.method == 'POST':
        selected_board = Board.objects.get(name=board_name)
        selected_column = selected_board.column_set.get(name=request.POST.get('column_name', None))
        task_title = request.POST.get('title', None)
        task_description = request.POST.get('description', None)
        
        selected_column.task_set.create(title=task_title, description=task_description, creation_date = timezone.now())

        columns = selected_board.column_set.all()
        
        context = {
                'board': selected_board,
                'columns': columns,
                }
        return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not allowed')


def delete_task(request, board_name):
    if request.method == 'POST':
        selected_board = Board.objects.get(name=board_name)
        selected_column = selected_board.column_set.get(name=request.POST.get('column_name', None))
        selected_task = selected_column.task_set.get(title=request.POST.get('task_title', None))
        
        selected_task.delete()
        
        columns = selected_board.column_set.all()

        context = {
                'board': selected_board,
                'columns': columns,
                }

        return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not allowed')

