import requests
from django.shortcuts import redirect, render
from django.http import Http404


def index(request):
    if request.method == 'GET':
        return render(request, 'welcome/index.html', {})
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        login_successful, message, email, full_name = login(email, password)

        if login_successful:
            return redirect('teamsapp:teams', email=email, full_name=full_name) 
        else:
            context = {'message': message}
            return render(request, 'welcome/index.html', context) 
    else:
        return Http404('Not allowed')


def login(email, password):
    full_name = ''
    try:
        response = requests.get("http://104.155.231.4:5000/authentication/", params={'email': email, 'password': password})
        
    except requests.exceptions.ConnectionError:
        message = "System unavailable"
        return False, message, email, full_name
    else:
        if response.status_code == 200:
            message = "Login succesfull"
            response = response.json()            
            email = response.get('data', {}).get('email')
            full_name = response.get('data', {}).get('full_name')
            return True, message, email, full_name
        else: 
            response = response.json()
            message = response.get('error', {}).get('description')
            return False, message, email, full_name

