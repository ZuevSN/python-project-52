from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from .models import Status
from .forms import StatusForm


class StatusListView(ListView):
    model = Status
    template_name = 'statuses/status_list.html'
    context_object_name = 'statuses'


class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status created')
    extra_context = {
        'operation': _('Create status'),
        'button_text': _('Create')
    }


class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status updated')
    extra_context = {
        'operation': _('Update status'),
        'button_text': _('Update')
    }

class StatusDeleteView(DeleteView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status updated')
    extra_context = {
        'operation': _('Delete status'),
        'button_text': _('Delete')
    }


