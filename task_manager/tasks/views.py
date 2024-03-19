from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import CreateTaskForm
from task_manager.service_tools.filters import TaskFilter
from django_filters.views import FilterView
from django.urls import reverse_lazy
from task_manager.service_tools.permissions import LoginRequired
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.service_tools.permissions import PermissionDeleteTaskRequired


# Create your views here.
TASKS_INDEX = reverse_lazy('tasks_index')


class TaskListView(LoginRequired, FilterView,
                   ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter


class TaskDetailView(LoginRequired, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    context_object_name = 'task'


class TaskCreateView(SuccessMessageMixin, LoginRequired,
                     CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'tasks/create.html'
    success_url = TASKS_INDEX

    success_message = _('Task is created successfully!')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, LoginRequired,
                     UpdateView):
    model = Task
    form_class = CreateTaskForm
    context_object_name = 'task'
    template_name = 'tasks/update.html'
    success_url = TASKS_INDEX

    success_message = _('Task is updated successfully!')


class TaskDeleteView(SuccessMessageMixin, LoginRequired,
                     PermissionDeleteTaskRequired, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/delete.html'
    success_url = TASKS_INDEX

    success_message = _('Task is deleted successfully!')
