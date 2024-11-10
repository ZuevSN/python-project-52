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
from .models import Label
from .forms import LabelForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import (
    CustomLoginRequiredMixin,
    DeleteProtectionMixin
)


class LabelListView(ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'


class LabelCreateView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    CreateView
):
    model = Label
    template_name = 'form.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label created')
    extra_context = {
        'header': _('Create label'),
        'button_text': _('Create')
    }


class LabelUpdateView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    UpdateView
):
    model = Label
    template_name = 'form.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Label updated')
    extra_context = {
        'header': _('Update label'),
        'button_text': _('Update')
    }

class LabelDeleteView(
    SuccessMessageMixin,
    CustomLoginRequiredMixin,
    DeleteProtectionMixin,
    DeleteView
):
    model = Label
    template_name = 'delete_form.html'
    form_class = LabelForm
    protect_message = _('Cannot delete because it is in use')
    protect_url = reverse_lazy('labels')
    success_url = reverse_lazy('labels')
    success_message = _('Label deleted')
    extra_context = {
        'header': _('Delete label'),
        'button_text': _('Delete')
    }


