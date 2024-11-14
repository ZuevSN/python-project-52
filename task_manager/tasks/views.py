from django.views.generic import (
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
    DeleteProtectionUserMixin
)
from django_filters.views import FilterView
from .filters import TaskFilter


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
    SuccessMessageMixin,
    NotLoggedMixin,
    CreateView
):
    model = Task
    template_name = 'form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('The task was created successfully')
    extra_context = {
        'header': _('Create task'),
        'button_text': _('Create')
    }

    def form_valid(self, form):
        form.instance.initiator = self.request.user
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
        'header': _('Update task'),
        'button_text': _('Update')
    }

#    def form_valid(self, form):
#        response = super().form_valid(form)
#        print("Form is valid. Task has been updated.")
#        print("Success message:", self.get_success_message(form))
        
#        return response
    
#    def form_invalid(self, form):
#        print("Form is invalid. Errors:", form.errors)
#        return super().form_invalid(form)


class TaskDeleteView(
    SuccessMessageMixin,
    NotLoggedMixin,
    DeleteProtectionUserMixin,
    DeleteView
):
    model = Task
    template_name = 'delete_form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('The task was successfully deleted')
    protect_message = _('Only the initiator of the task can delete it.')
    protect_url = reverse_lazy('tasks')
    extra_context = {
        'header': _('Delete task'),
        'button_text': _('Yes, delete')
    }
