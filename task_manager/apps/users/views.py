from .models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import CreateUserForm, UpdateUserForm
from task_manager.service_tools.permissions import (PermissionChangeUserRequired,
                                                    DeletionRestricted,
                                                    LoginRequired)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


USERS_INDEX = reverse_lazy('users_index')


class IndexView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


class CreateUserView(SuccessMessageMixin, CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User has been registered successfully')


class UpdateUserView(SuccessMessageMixin, PermissionChangeUserRequired,
                     LoginRequired, UpdateView):
    model = User
    context_object_name = 'user'
    form_class = UpdateUserForm
    template_name = 'users/update.html'
    success_url = USERS_INDEX
    initial = {'password': ''}
    success_message = _('User successfully updated')


class DeleteUserView(SuccessMessageMixin, LoginRequired,
                     DeletionRestricted,
                     PermissionChangeUserRequired, DeleteView):
    model = User
    context_object_name = 'user'
    template_name = 'users/delete.html'

    success_url = USERS_INDEX
    success_message = _('User successfully deleted')

    reject_url = USERS_INDEX
    reject_message = _('Unable to delete user because it is in use')
