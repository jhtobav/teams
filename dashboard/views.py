
from django.shortcuts import redirect, render, Http404

from .models import Board, Column, Task


def dashboard(request):
    if request.method == 'GET':
        boards = Board.objects.all()
        context = {'boards': boards}
        return render(request, 'dashboard/dashboard.html', context)
    else:
        return Http404('Not allowed')


def board(request, board_name):
    selected_board = Board.objects.get(name=board_name)
    columns = selected_board.column_set.all()
    context = {
            'board': selected_board,
            'columns': columns,
            }
    return render(request, 'dashboard/board.html', context)

