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
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import (
    NotLoggedMixin,
    DeleteProtectionMixin
)


class StatusListView(
    NotLoggedMixin,
    ListView
):
    model = Status
    template_name = 'statuses/status_list.html'
    context_object_name = 'statuses'


class StatusCreateView(
    SuccessMessageMixin,
    NotLoggedMixin,
    CreateView
):
    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('The status was created successfully')
    extra_context = {
        'header': _('Creating a status'),
        'button_text': _('Create')
    }


class StatusUpdateView(
    SuccessMessageMixin,
    NotLoggedMixin,
    UpdateView
):
    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('The status has been successfully changed')
    extra_context = {
        'header': _('Changing the status'),
        'button_text': _('Change')
    }


class StatusDeleteView(
    DeleteProtectionMixin,
    SuccessMessageMixin,
    NotLoggedMixin,
    DeleteView
):
    model = Status
    template_name = 'delete_form.html'
    success_url = reverse_lazy('statuses')
    success_message = _('The status was successfully deleted')
    delete_protection_message = _(
        'It is not possible to delete status because it is being used'
    )
    delete_protection_url = reverse_lazy('statuses')
    extra_context = {
        'header': _('Deleting a status'),
        'button_text': _('Yes, delete')
    }
