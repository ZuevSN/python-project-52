import django_filters as df
from django.utils.translation import gettext_lazy as _
from django import forms
from task_manager.users.models import CustomUser
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TaskFilter(df.FilterSet):
    user_tasks = df.BooleanFilter(
        label=_('show my tasks'),
        method='show_user_tasks',
        widget=forms.CheckboxInput()
    )
    status = df.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_('status')
    )
    executor = df.ModelChoiceFilter(
        queryset=CustomUser.objects.all(),
        label=_('executor')
    )
    labels = df.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('label')
    )

    def show_user_tasks(
        self, queryset, name_filter, check
    ):
        if check:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'user_tasks']
