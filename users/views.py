from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomRegisterForm
from .models import CustomUser

def register_view(request):
    form = CustomRegisterForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            print(form.errors)  # ✅ теперь безопасно

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/users/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_list_view(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'user_list': users})


def logout_view(request):
    logout(request)
    return redirect('/login/')