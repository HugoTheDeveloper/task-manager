from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.apps.tasks.models import Task
from django.contrib.auth.mixins import AccessMixin
from django.db.models import ProtectedError


class NoPermissionMixin(UserPassesTestMixin):
    message_txt = None
    reject_url = None

    def handle_no_permission(self):
        messages.error(self.request, self.message_txt) # noqa
        return redirect(self.reject_url)


class PermissionChangeUserRequired(NoPermissionMixin):
    message_txt = _("You haven't permission to edit or delete this user!")
    reject_url = reverse_lazy('users_index')

    def test_func(self):
        user_id_to_change = self.kwargs.get('pk') # noqa
        return self.request.user.pk == user_id_to_change # noqa


class PermissionDeleteTaskRequired(NoPermissionMixin):
    message_txt = _("Only the author of the task can delete it")
    reject_url = reverse_lazy('tasks_index')

    def test_func(self):
        task_id = self.kwargs.get('pk') # noqa
        task = Task.objects.get(pk=task_id) # noqa
        creator_id = task.author.pk
        user_id = self.request.user.pk # noqa
        return creator_id == user_id


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
