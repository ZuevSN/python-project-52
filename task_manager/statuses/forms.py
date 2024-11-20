from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Status


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ['name']


class StatusesForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(StatusesForm, self).__init__(*args, **kwargs)
        self.statuses = Status.objects.all()
        for status in self.statuses:
            self.fields[f'status_{status.id}'] = forms.CharField(
                label=status.name,
                initial=status.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                disabled=True,
            )
            self.fields[f'created_at_{status.id}'] = forms.CharField(
                label=_('Created At'),
                initial=status.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                disabled=True,
            )
