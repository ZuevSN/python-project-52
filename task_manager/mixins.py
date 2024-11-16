from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


class NotLoggedMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        error_message = _('You are not logged in! Please log in.')
        error_url = reverse_lazy('login')
        if not request.user.is_authenticated:
            messages.error(request, error_message)
            return redirect(error_url)
        return super().dispatch(request, *args, **kwargs)


class PermitModifyOtherUser(UserPassesTestMixin):

    def test_func(self):
        return self.get_object().id == self.request.user.id

    def handle_no_permission(self):
        error_message = _('You dont have permissions to modify another user.')
        error_url = reverse_lazy('users')
        messages.error(self.request, error_message)
        return redirect(error_url)


class DeleteProtectionTaskMixin(UserPassesTestMixin):

    def test_func(self):
        obj = self.get_object()
        return obj is not None and obj.author == self.request.user

    def handle_no_permission(self):
        error_message = _('Only the author of the task can delete it.')
        error_url = reverse_lazy('tasks')
        print(f":User  {self.request.user}")
        messages.error(self.request, error_message)
        return redirect(error_url)


class DeleteProtectionMixin:
    delete_protection_message = None
    delete_protection_url = None

    def has_dependencies(self, obj):
        for related_field in obj._meta.get_fields():
            if related_field.one_to_many or related_field.one_to_one:
                accessor_name = related_field.get_accessor_name()
                related_queryset = getattr(obj, accessor_name)
                if related_queryset.exists():
                    return True
            elif related_field.many_to_many:
                related_manager = getattr(obj, related_field.name)
                if related_manager.exists():
                    return True
        return False

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.has_dependencies(obj):
            messages.error(request, self.delete_protection_message)
            return redirect(self.delete_protection_url)
        else:
            return super().post(request, *args, **kwargs)
