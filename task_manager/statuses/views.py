from .models import Status
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import CreateStatusForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.service_tools.permissions import (LoginRequired,
                                                    DeletionRestricted)

# Create your views here.
STATUS_INDEX = reverse_lazy('status_index')


class ListStatusView(LoginRequired, ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'status/index.html'


class CreateStatusView(SuccessMessageMixin, LoginRequired,
                       CreateView):
    model = Status
    template_name = 'status/create.html'
    form_class = CreateStatusForm
    success_url = STATUS_INDEX

    success_message = _('Status is created successfully!')


class UpdateStatusView(SuccessMessageMixin, LoginRequired,
                       UpdateView):
    model = Status
    context_object_name = 'status'
    template_name = 'status/update.html'
    form_class = CreateStatusForm
    success_url = STATUS_INDEX

    success_message = _("Status is updated successfully!")


class DeleteStatusView(SuccessMessageMixin, LoginRequired,
                       DeletionRestricted, DeleteView):
    model = Status
    context_object_name = 'status'
    template_name = 'status/delete.html'
    success_url = STATUS_INDEX
    reject_url = STATUS_INDEX

    success_message = _("Status is deleted successfully!")
    reject_message = _('Unable to delete status because it is in use')
