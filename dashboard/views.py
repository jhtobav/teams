from django.shortcuts import render
from . import models

def dashboard(request):
    boards = models.Board.objects.all()
    columns = models.Column.objects.all()
    tasks = models.Task.objects.all()

    context = {
            'dashboards': boards,
            'columns': columns,
            'tasks': tasks,
            }
    return render(request, 'dashboard/dashboard.html', context)
