
from django.shortcuts import redirect, render, Http404
from django.utils import timezone

from .models import Board, Column, Task


def dashboard(request):
    if request.method == 'GET':
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
    elif request.method == 'POST':
        title = request.POST.get('title', None)
        description = request.POST.get('description', None)
        creation_date = timezone.now() 
        selected_board = Board.objects.get(name=board_name)
        column_name = request.POST.get('column_name', None)
        print(column_name)
        selected_column = selected_board.column_set.all().get(name=column_name)
        new_task = Task.objects.create(Column=column, title=title, description=description, creation_date=creation_date)
        context = {'message': 'Created!'}
        return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not allowd')

