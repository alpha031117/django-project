from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class UserSignUp(generic.CreateView):
    template_name = "accounts/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('authentication:login-page')


class UserSignIn(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('blog-home')

class UserLogOut(LogoutView):
    next_page = reverse_lazy('blog-home')
