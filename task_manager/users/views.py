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
    NotLoggedMixin,
    PermitModifyOtherUser,
    DeleteProtectionMixin
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
    success_message = _('The user was created successfully')
    extra_context = {
        'header': _('Registration'),
        'button_text': _('Register')
    }


class UserUpdateView(
    SuccessMessageMixin,
    NotLoggedMixin,
    PermitModifyOtherUser,
    UpdateView
):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'form.html'
    success_url = reverse_lazy('users')
    success_message = _('The user has been successfully changed')
    extra_context = {
        'header': _('Changing the user'),
        'button_text': _('Change')
    }


class UserDeleteView(
    NotLoggedMixin,
    PermitModifyOtherUser,
    DeleteProtectionMixin,
    SuccessMessageMixin,
    DeleteView
):
    model = CustomUser
    template_name = 'delete_form.html'
    success_url = reverse_lazy('users')
    success_message = _('The user was successfully deleted')
    delete_protection_message = _(
        'It is not possible to delete a user because it is being used'
    )
    delete_protection_url = reverse_lazy('users')
    extra_context = {
        'header': _('Deleting a user'),
        'button_text': _('Yes, delete')
    }
