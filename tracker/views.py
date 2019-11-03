from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Homework

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    homework = Homework.objects.filter(user=request.user.id)
    return render(request, 'tracker/home.html', {"homework": homework})

def about(request):
    return render(request, 'tracker/about.html', {})

@login_required(login_url='/accounts/login/')
def account(request):
    return render(request, "tracker/account.html", {})