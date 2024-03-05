from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    label_set = models.ManyToManyField(Label, through='Membership')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, null=True,
                                 blank=True, related_name='tasks_todo')
    created_at = models.DateTimeField(auto_now_add=True)


class Membership(models.Model):
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
