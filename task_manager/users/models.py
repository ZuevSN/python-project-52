from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    USER_TYPE = (
        ('specialist', _('Specialist')),
        ('manager', _('Manager')),
    )

    user_type = models.CharField(
        max_length=100,
        choices=USER_TYPE,
        default='specialist',
        verbose_name=_('User type')
    )
    def __str__(self):
        return self.get_full_name()
    

