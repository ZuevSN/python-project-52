from django.shortcuts import render
from django.views.generic import (
    TemplateView
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from django.contrib.auth.forms import AuthenticationForm

from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'

class UserLoginView(LoginView):
    template_name = 'form.html'
    form_class = AuthenticationForm
    extra_context = {
        'header': _('Logon'),
        'button_text': _('Sign in')
    }
    next_page = reverse_lazy('index')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')