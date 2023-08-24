from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserLoginForm
from django.urls import reverse_lazy
from django.views import View


# Create your views here.
class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'auth_user/registration.html'
    success_url = reverse_lazy('main')


class LoginUser(LoginView):
    form_class = UserLoginForm  # AuthenticationForm
    template_name = 'auth_user/login_user.html'
    success_url = reverse_lazy('main')


def logout_fun(request):
    logout(request)
    return redirect('log')
