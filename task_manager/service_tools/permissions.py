from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from task_manager.tasks.models import Task


class PermissionChangeUserRequired(UserPassesTestMixin):
    def test_func(self):
        user_id_to_change = self.kwargs.get('pk') # noqa
        return self.request.user.pk == user_id_to_change # noqa

    def handle_no_permission(self):
        message_txt = _("You haven't permission to edit or delete this user!")
        messages.error(self.request, message_txt) # noqa
        return redirect('users_index')


class PermissionDeleteTaskRequired(UserPassesTestMixin):
    def test_func(self):
        task_id = self.kwargs.get('pk') # noqa
        task = Task.objects.get(pk=task_id) # noqa
        creator_id = task.author.pk
        user_id = self.request.user.pk # noqa
        return creator_id == user_id

    def handle_no_permission(self):
        message_txt = _("You haven't permission to delete this task!")
        messages.error(self.request, message_txt) # noqa
        return redirect('tasks_index')
