from django.urls import path

from . import views


app_name = 'dashboard'
urlpatterns = [
    path('<str:team_name>', views.dashboard, name='dashboard'),
    path('board/<str:board_name>', views.board, name='board'),
    path('board/<str:board_name>/delete_board', views.delete_board, name ='delete_board'),
    path('board/<str:board_name>/create_column', views.create_column, name='create_column'),
    path('board/<str:board_name>/delete_column', views.delete_column, name='delete_column'),
    path('board/<str:board_name>/create_task', views.create_task, name='create_task'),
    path('board/<str:board_name>/delete_task', views.delete_task, name='delete_task')

]
