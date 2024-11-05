from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class IndexView(TemplateView):
    template_name = 'index.html'


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('login')


class UserUpdateView(UpdateView):
    mpdel = User
    form_class = UserCreationForm
    template_name = 'edit_user.html'
    success_url = reverse_lazy('user_list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('user_list')

#def index(request):
#    return render(request, 'index.html', context={
#        'who': 'World',
#    })