from django.urls import path

from . import views


app_name = 'teamsapp'
urlpatterns = [
    path('', views.teams, name='teams'),
    path('create_team', views.create_team, name='create_team')
]

