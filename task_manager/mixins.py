from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not logged in! Please log in.'))
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)

class CustomUserPassesTestMixin(UserPassesTestMixin):
    protect_message = None
    protect_url = None

    def test_func(self):
        return self.get_object().id == self.request.user.id
    
    def handle_no_permission(self):
        messages.error(self.request, self.protect_message)
        return redirect(self.protect_url)

class DeleteProtectionUserMixin(UserPassesTestMixin):
    protect_message = None
    protect_url = None

    def test_func(self):
        obj = self.get_object()
#        print(f":User  {self.request.user}, Initiator: {obj.initiator}")
        return obj is not None and obj.initiator == self.request.user
    
    def handle_no_permission(self):
        print(f":User  {self.request.user}")
        messages.error(self.request, self.protect_message)
        return redirect(self.protect_url)

class DeleteProtectionMixin:
    protect_message = None
    protect_url = None

    def has_related_objects(self, obj):
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
        if self.has_related_objects(obj):
            messages.error(request, self.protect_message)
            return redirect(self.protect_url)
        else:
            messages.success(request, _('test Label deleted')) 
            return super().post(request, *args, **kwargs)

