from django.shortcuts import redirect, render
from django.http import Http404


def index(request):
    if request.method == 'GET':
        return render(request, 'welcome/index.html', {})
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if login(email, password):
            return redirect('teamsapp:teams') 
        else:
            context = { 'message': 'Wrong credentials' }
            return render(request, 'welcome/index.html', context) 
    else:
        return Http404('Not allowed')


def login(email, password):
    return True
