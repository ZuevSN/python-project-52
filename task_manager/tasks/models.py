from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import CustomUser
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Name')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )

    description = models.TextField(
        verbose_name=_('Description'),
        blank=True
    )
    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name=_('Executor')
    )
    initiator = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name=_('Initiator')
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name=_('Initiator')
    )
    labels = models.ManyToManyField(
        Label
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Tasks')