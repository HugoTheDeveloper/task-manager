# from django.shortcuts import render, redirect
# from django.views import View
from .models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import CreateUserForm
from task_manager.service_tools.permissions import PermissionChangeUserRequired
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'

# class IndexView(View):
#     @staticmethod
#     def get(request, *args, **kwargs):
#         users = User.objects.all()
#         return render(request, 'users/index.html',
#                       {'users': users})


class CreateUserView(SuccessMessageMixin, CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User was successfully created!')


# class CreateView(View):
#
#     @staticmethod
#     def get(request, *args, **kwargs):
#         form = CreateUserForm()
#         return render(request, 'users/create.html', {'form': form})
#
#     @staticmethod
#     def post(request, *args, **kwargs):
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users_index')
#         return render(request, 'users/create.html', {'form': form})


class UpdateUserView(SuccessMessageMixin, PermissionChangeUserRequired,
                     LoginRequiredMixin, UpdateView):
    model = User
    context_object_name = 'user'
    form_class = CreateUserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users_index')
    initial = {'password': ''}
    success_message = _('User was successfully updated!')


class DeleteUserView(SuccessMessageMixin, PermissionChangeUserRequired,
                     LoginRequiredMixin, DeleteView):
    model = User
    context_object_name = 'user'
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User was successfully deleted!')
