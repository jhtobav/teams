from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('board/<str:board_name>', views.board, name='board'),
    path('board/<str:board_name>/create_column', views.create_column, name='create_column'),
    path('board/<str:board_name>/create_task', views.create_task, name='create_task'),
    path('board/<str:board_name>/delete_task', views.delete_task, name='delete_task')

]
