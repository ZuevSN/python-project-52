from django.shortcuts import render
from django.views.generic import (
    TemplateView
)
from django.contrib.auth.views import LoginView

from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'

class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class HomeView(TemplateView):
    template_name = 'home.html'