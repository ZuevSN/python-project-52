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


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task created')
    extra_context = {
        'header': _('Create task'),
        'button_text': _('Create')
    }


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task updated')
    extra_context = {
        'header': _('Update task'),
        'button_text': _('Update')
    }

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete_form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task deleted')
    extra_context = {
        'header': _('Delete task'),
        'button_text': _('Yes, delete')
    }

