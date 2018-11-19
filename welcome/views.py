from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'welcome/index.html', context)

def go_to_boards(request):
    return redirect("dashboard")

