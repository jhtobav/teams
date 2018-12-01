# search/urls.py
from django.urls import path
  
from . import views


app_name = 'search'
urlpatterns = [
    path('search_team_boards/', views.search_team_boards, name='search_team_boards'),
    path('search_teams/', views.search_teams, name='search_teams')
]

