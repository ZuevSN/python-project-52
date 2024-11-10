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
from .models import Status
from .forms import StatusForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import (
    CustomLoginRequiredMixin,
    DeleteProtectionMixin
)


class StatusListView(
    CustomLoginRequiredMixin,
    ListView
):
    model = Status
    template_name = 'statuses/status_list.html'
    context_object_name = 'statuses'


class StatusCreateView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    CreateView
):
    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status created')
    extra_context = {
        'header': _('Create status'),
        'button_text': _('Create')
    }


class StatusUpdateView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    UpdateView
):
    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status updated')
    extra_context = {
        'header': _('Update status'),
        'button_text': _('Update')
    }

class StatusDeleteView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    DeleteProtectionMixin,
    DeleteView
):
    model = Status
    template_name = 'delete_form.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status deleted')
    protect_message = _('Cannot delete because it is in use')
    protect_url = reverse_lazy('statuses')
    extra_context = {
        'header': _('Delete status'),
        'button_text': _('Yes, delete')
    }


