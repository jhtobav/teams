from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('go_to', views.go_to_teams, name='go_to_teams'),
]
