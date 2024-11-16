from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True
        self.fields['username'].help_text = _(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        )
        self.fields['password1'].help_text = _(
            'Your password must contain at least 3 characters.'
        )
        self.fields['password2'].help_text = _(
            'Enter the same password as before, for verification.'
        )

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 3:
            raise forms.ValidationError(
                _('The entered password is too short. \
                  It must contain at least 3 characters.')
            )
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('The entered passwords do not match.'))
        return password2

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        ]
