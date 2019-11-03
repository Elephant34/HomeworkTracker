from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form":form})

def delete(request):
    request.user.is_active = False
    request.user.save()
    logout(request)
    return render(request, "delete.html", {})