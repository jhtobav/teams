# teamsapp/urls.py
from django.urls import path

from . import views


app_name = 'teamsapp'
urlpatterns = [
    path('', views.teams, name='teams'),
    path('update_member_teams/<str:team_name>', views.update_member_teams, name='update_member_teams'),
    path('create_team', views.create_team, name='create_team')
]

