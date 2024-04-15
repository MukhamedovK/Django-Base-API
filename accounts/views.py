from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import User
from .utils import registration_check


def login_page(request):
    if not request.user.is_authenticated:
        context = {}
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("routerAPI")
            
            context["error"] = "Incorrect username or password"
        return render(request, "login.html", context=context)
    else:
        return redirect("routerAPI")


def register_page(request):
    if not request.user.is_authenticated:
        context = {}
        if request.method == "POST":
            name = request.POST.get("name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password")
            
            error = registration_check(formData=request.POST)
            if error is None:
                user = User.objects.create_user(
                    name=name,
                    username=username,
                    password=password1,
                    email=email,
                )
                User.objects.create(user=user)
                login(request, user)
                return redirect("routerAPI")
            else:
                context['error'] = error
        return render(request, "register.html", context=context)
    else:
        return redirect("routerAPI")


def logout_page(request):
    logout(request)
    return redirect("login")
