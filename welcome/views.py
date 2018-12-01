# welcome/views.py
import requests
from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages


def index(request):
    """
       Renders the index page of the teams app
    """
    if request.method == 'GET':
        return render(request, 'welcome/index.html', {})
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        login_successful, message, email, full_name = login(email, password)

        if login_successful:
            messages.add_message(request, messages.INFO, message)
            return redirect('teamsapp:teams', email=email, full_name=full_name) 
        else:
            messages.add_message(request, messages.INFO, message)
            return redirect('welcome:index') 
    else:
        return Http404('Not allowed')


def login(email, password):
    """
        Calls the flask authentication micro-service
    """
    full_name = ''
    try:
        response = requests.get("http://104.155.231.4:5000/authentication/",
                                params={'email': email, 'password': password})
        
    except requests.exceptions.ConnectionError:
        message = "System unavailable"
        return False, message, email, full_name
    else:
        if response.status_code == 200:
            response = response.json()            
            message = "Login successful"
            email = response.get('data', {}).get('email')
            full_name = response.get('data', {}).get('full_name')
            return True, message, email, full_name
        else: 
            response = response.json()
            message = response.get('error', {}).get('description')
            return False, message, email, full_name

