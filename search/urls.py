from django.urls import path
  
from . import views


app_name = 'search'
urlpatterns = [
    path('<str:team_name>', views.search, name='search'),
    path('search_team_boards/', views.search_team_boards, name='search_team_boards'),
    path('search_teams/', views.search_teams, name='search_teams')
]

