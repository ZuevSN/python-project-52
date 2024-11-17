from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import (
    NotLoggedMixin,
    DeleteProtectionTaskMixin
)
from django_filters.views import FilterView
from .filters import TaskFilter


class TaskDetailView(
    NotLoggedMixin,
    DetailView
):
    model = Task
    template_name = 'tasks/task_info.html'


class TaskListView(
    NotLoggedMixin,
    FilterView
):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    extra_context = {
        'button_text': _('Filter')
    }


class TaskCreateView(
    NotLoggedMixin,
    SuccessMessageMixin,
    CreateView
):
    model = Task
    template_name = 'form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('The task was created successfully')
    extra_context = {
        'header': _('Creating a task'),
        'button_text': _('Create')
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(
    NotLoggedMixin,
    SuccessMessageMixin,
    UpdateView
):
    model = Task
    template_name = 'form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('The task has been successfully changed')
    extra_context = {
        'header': _('Changing the task'),
        'button_text': _('Change')
    }


class TaskDeleteView(
    NotLoggedMixin,
    DeleteProtectionTaskMixin,
    SuccessMessageMixin,
    DeleteView
):
    model = Task
    template_name = 'delete_form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('The task was successfully deleted')
    extra_context = {
        'header': _('Deleting a task'),
        'button_text': _('Yes, delete')
    }
