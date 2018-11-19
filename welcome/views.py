from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requesr):
    return HttpResponse("Welcome to the Teams application")

