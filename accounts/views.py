from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


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

@login_required(login_url='/accounts/login/')
def delete(request):
    request.user.is_active = False
    request.user.save()
    logout(request)
    return render(request, "delete.html", {})
