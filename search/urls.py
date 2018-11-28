from django.urls import path
  
from . import views


app_name = 'search'
urlpatterns = [
    path('/<str:team_name>', views.search, name='search'),
    path(r'^ajax/validate_username/$' , views.search_engine, name='search_engine')
]

