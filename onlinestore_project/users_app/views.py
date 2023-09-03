from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from product_app.utils import DataMixin
from users_app.forms import CustomUserCreationForm, CustomAuthenticationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/register.html"


class CustomLoginView(DataMixin, LoginView):
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy("home")


