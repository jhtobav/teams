from django.shortcuts import render


def dashboard(request):
    context = {'message': "saludos desde dashboard"}
    return render(request, 'dashboard/dashboard.html', context)
