from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.utils.safestring import mark_safe

class CustomUserCreationForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True
        self.fields['password1'].help_text = mark_safe(
            '<ul>'
            '<li>Ваш пароль должен содержать как минимум 3 символа.</li>'
            '</ul>'
        )

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 3:
            raise forms.ValidationError('Введённый пароль слишком короткий. Он должен содержать как минимум 3 символа.')
        return password
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Введенные пароли не совпадают.')
        return password2
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']