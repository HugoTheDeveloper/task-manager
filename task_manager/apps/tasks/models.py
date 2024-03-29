from django.db import models
from task_manager.apps.users.models import User
from task_manager.apps.statuses.models import Status
from task_manager.apps.labels.models import Label
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                               verbose_name=_('Status'))
    label_set = models.ManyToManyField(Label, through='Membership', blank=True)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, null=True,
                                 blank=True, related_name='tasks_todo',
                                 verbose_name=_('Executor'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Task')


class Membership(models.Model):
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
