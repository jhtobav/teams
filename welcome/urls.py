# welcome/urls.py
from django.urls import path

from . import views


app_name = 'welcome'
urlpatterns = [
        path('', views.index, name='index'),
        path('logout', views.logout, name='logout')
]
