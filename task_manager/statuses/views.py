from .models import Status
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import CreateStatusForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
STATUS_INDEX = reverse_lazy('status_index')


class ListStatusView(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'status/index.html'


class CreateStatusView(SuccessMessageMixin, LoginRequiredMixin,
                       CreateView):
    model = Status
    template_name = 'status/create.html'
    form_class = CreateStatusForm
    success_url = STATUS_INDEX

    success_message = _('Status is created successfully!')


class UpdateStatusView(SuccessMessageMixin, LoginRequiredMixin,
                       UpdateView):
    model = Status
    context_object_name = 'status'
    template_name = 'status/update.html'
    form_class = CreateStatusForm
    success_url = STATUS_INDEX

    success_message = _("Status is updated successfully!")


class DeleteStatusView(SuccessMessageMixin, LoginRequiredMixin,
                       DeleteView):
    model = Status
    context_object_name = 'status'
    template_name = 'status/delete.html'
    success_url = STATUS_INDEX

    success_message = _("Status is deleted successfully!")
