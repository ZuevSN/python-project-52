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
from .forms import StatusForm, StatusesForm, UniversalForm


class GenericListView(View):
    model = None
    fields = []
    def get(self, request, *args, **kwargs):
        instances = self.model.objects.all()
        return render(request, 'dataframe_template.html', {
            'instances': instances,
            'fields': self.fields,
        })

class UniversalListView(View):
    model = None
    
    def get(self, request, *args, **kwargs):
        header = self.model._meta.verbose_name
        objects = self.model.objects.all()
        form = UniversalForm(self.model)
        context = {
            'header': header,
            'objects': objects,
            'form': form,
        }
        return render(request, 'dataframe_template.html', context)

    @classmethod
    def as_view(cls, **initkwargs):
        model = initkwargs.pop('model', None)  # Извлекаем модель из аргументов
        if model is not None:
            cls.model = model  # Устанавливаем модель как атрибут класса
        return super().as_view(**initkwargs)

class StatusListView(UniversalListView):
    model = Status
#class StatusListView(ListView):
#    model = Status
#    template_name = 'statuses/status_list.html'
#    context_object_name = 'statuses'
#class StatusListView(View):
#    def get(self, request, *args, **kwargs):
#        form = StatusesForm
#        return render(request, 'dataframe_template.html', {'form': form})



class StatusCreateView(CreateView):
    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status created')
    extra_context = {
        'header': _('Create status'),
        'button_text': _('Create')
    }


class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status updated')
    extra_context = {
        'header': _('Update status'),
        'button_text': _('Update')
    }

class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status updated')
    extra_context = {
        'header': _('Delete status'),
        'button_text': _('Delete')
    }


