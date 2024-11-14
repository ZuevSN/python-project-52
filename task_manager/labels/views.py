from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from .models import Label
from .forms import LabelForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import (
    NotLoggedMixin,
    DeleteProtectionMixin
)


class LabelListView(ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'


class LabelCreateView(
    SuccessMessageMixin,
    NotLoggedMixin,
    CreateView
):
    model = Label
    template_name = 'form.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('The label was created successfully')
    extra_context = {
        'header': _('Create label'),
        'button_text': _('Create')
    }


class LabelUpdateView(
    SuccessMessageMixin,
    NotLoggedMixin,
    UpdateView
):
    model = Label
    template_name = 'form.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully changed')
    extra_context = {
        'header': _('Update label'),
        'button_text': _('Update')
    }


class LabelDeleteView(
    SuccessMessageMixin,
    NotLoggedMixin,
    DeleteProtectionMixin,
    DeleteView
):
    model = Label
    template_name = 'delete_form.html'
    success_url = reverse_lazy('labels')
    success_message = _('The label was successfully deleted')
    protect_message = _(
        'It is not possible to delete, because it is being used'
    )
    protect_url = reverse_lazy('labels')
    extra_context = {
        'header': _('Delete label'),
        'button_text': _('Delete')
    }
