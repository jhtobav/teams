
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
    elif request.method == 'POST':
        title = request.POST.get('title', None)
        if title:
            description = request.POST.get('description', None)
            creation_date = timezone.now() 
  
            selected_board = Board.objects.get(name=board_name)
            columns = selected_board.column_set.all()
  
            column_name = request.POST.get('column_name', None)
            selected_column = selected_board.column_set.all().get(name=column_name)
            selected_column.task_set.create(title=title, description=description, creation_date=creation_date)
            context = {
                   'board': selected_board,
                   'columns': columns,
                   }
        else:
            selected_board = Board.objects.get(name=board_name)

            column_name = request.POST.get('name', None)
            column_index = request.POST.get('index', None)
            
            selected_board.column_set.create(name=column_name, index=column_index)
            columns = selected_board.column_set.all()

            context = {
                    'board': selected_board,
                    'columns': columns,
                    }
        return render(request, 'dashboard/board.html', context)
    else:
        return Http404('Not allowd')

