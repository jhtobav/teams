import requests
from django.shortcuts import redirect, render
from django.http import Http404


def index(request):
    if request.method == 'GET':
        return render(request, 'welcome/index.html', {})
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        login_successful, message  = login(email, password)

        context = {'message': message}

        if login_successful:
            return redirect('teamsapp:teams') 
        else:
            return render(request, 'welcome/index.html', context) 
    else:
        return Http404('Not allowed')


def login(email, password):
    try:
        response = requests.get("http://104.155.231.4:5000/authentication/", params={'email': email, 'password': password})
    except requests.exceptions.ConnectionError:
        message = "System unavailable"
        return False, message
    else:
        if response.status_code == 200:
            message = "Login succesfull"
            return True, message
        else: 
            response = response.json()
            message = response.get('error', {}).get('description')
            return False, message

