from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomRegisterForm
from .models import CustomUser
from django.views import View
from django.views.generic import ListView


class RegisterView(View):
    def get(self, request):
        form = CustomRegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            print(form.errors)  # ✅ теперь безопасно
            return render(request, 'register.html', {'form': form})
# def register_view(request):
#     form = CustomRegisterForm(request.POST or None, request.FILES or None)

#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('/login/')
#         else:
#             print(form.errors)  # ✅ теперь безопасно

#     return render(request, 'register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/users/')
        return render(request, 'login.html', {'form': form})

# def login_view(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect('/users/')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')

# def user_list_view(request):
#     users = CustomUser.objects.all()
#     return render(request, 'user_list.html', {'user_list': users})

class UserListView(ListView):
    model = CustomUser
    template_name = 'user_list.html'
    context_object_name = 'user_list'

# def logout_view(request):
#     logout(request)
#     return redirect('/login/')