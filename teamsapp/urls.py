# teamsapp/urls.py
from django.urls import path

from . import views


app_name = 'teamsapp'
urlpatterns = [
    path('<str:email>&<str:full_name>', views.teams, name='teams'),
    path('<str:email>/update_member_teams/<str:team_name>', views.update_member_teams, name='update_member_teams'),
    path('<str:email>/create_team', views.create_team, name='create_team')
]

