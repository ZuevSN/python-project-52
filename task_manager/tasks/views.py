from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views import View

from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import (
    CustomLoginRequiredMixin,
    CustomUserPassesTestMixin
)


class TaskListView(
    CustomLoginRequiredMixin,
    ListView
):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    CreateView
):
    model = Task
    template_name = 'form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task created')
    extra_context = {
        'header': _('Create task'),
        'button_text': _('Create')
    }


class TaskUpdateView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    UpdateView
):
    model = Task
    template_name = 'form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task updated')
    extra_context = {
        'header': _('Update task'),
        'button_text': _('Update')
    }

class TaskDeleteView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    CustomUserPassesTestMixin,
    DeleteView
):
    model = Task
    template_name = 'delete_form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task deleted')
    protect_message = _("Task can be deleted only by initiator")
    protect_url = reverse_lazy('tasks')
    extra_context = {
        'header': _('Delete task'),
        'button_text': _('Yes, delete')
    }


