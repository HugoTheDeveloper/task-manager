from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.tasks.models import Task
from django.contrib.auth.mixins import AccessMixin
from django.db.models import ProtectedError


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
        message_txt = _("Only the author of the task can delete it")
        messages.error(self.request, message_txt) # noqa
        return redirect('tasks_index')


class LoginRequired(AccessMixin):
    err_message = _('You are not logged in! Please log in.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.err_message)
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs) # noqa


class DeletionRestricted:
    reject_message = None
    reject_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs) # noqa
        except ProtectedError:
            messages.error(request, self.reject_message)
            return redirect(self.reject_url)
