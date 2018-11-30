# dashboard/urls.py
from django.urls import path

from . import views


app_name = 'dashboard'
urlpatterns = [
    path('<str:team_name>', views.dashboard, name='dashboard'),
    path('<str:team_name>/create_board', views.create_board, name='create_board'),
    path('<str:team_name>/board/<str:board_name>', views.board, name='board'),
    path('<str:team_name>/board/<str:board_name>/delete_board', views.delete_board, name ='delete_board'),
    path('<str:team_name>/board/<str:board_name>/create_column', views.create_column, name='create_column'),
    path('<str:team_name>/board/<str:board_name>/delete_column', views.delete_column, name='delete_column'),
    path('<str:team_name>/board/<str:board_name>/create_task', views.create_task, name='create_task'),
    path('<str:team_name>/board/<str:board_name>/move_task_right', views.move_task_right, name='move_task_right'),
    path('<str:team_name>/board/<str:board_name>/move_task_left', views.move_task_left, name='move_task_left'),
    path('<str:team_name>/board/<str:board_name>/delete_task', views.delete_task, name='delete_task')
]
