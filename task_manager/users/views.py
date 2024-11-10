from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import (
    CustomLoginRequiredMixin,
    CustomUserPassesTestMixin
)


class UserListView(ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserCreateView(
    SuccessMessageMixin,
    CreateView
):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')
    success_message = _('User created')
    extra_context = {
        'header': _('Create user'),
        'button_text': _('Create')
    }


class UserUpdateView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    CustomUserPassesTestMixin,
    UpdateView
):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'form.html'
    success_url = reverse_lazy('users')
    protect_message = _("You don't have permissions to modify another user.")
    protect_url = reverse_lazy('users')


class UserDeleteView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    CustomUserPassesTestMixin,
    DeleteView
):
    model = CustomUser
    template_name = 'delete_form.html'
    success_url = reverse_lazy('users')
    success_message = _('User deleted')
    protect_message = _("You don't have permissions to modify another user.")
    protect_url = reverse_lazy('users')
    extra_context = {
        'header': _('Delete user'),
        'button_text': _('Yes, delete')
    }
