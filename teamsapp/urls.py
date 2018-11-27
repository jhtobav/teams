from django.urls import path

from . import views


app_name = 'teamsapp'
urlpatterns = [
    path('<str:email>', views.teams, name='teams'),
    path('<str:email>/create_team', views.create_team, name='create_team')
]

