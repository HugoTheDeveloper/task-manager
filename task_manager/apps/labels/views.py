from .models import Label
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import LabelCreateForm
from django.urls import reverse_lazy
from task_manager.service_tools.permissions import (LoginRequired,
                                                    DeletionRestricted)
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
LABEL_INDEX = reverse_lazy('labels_index')


class ListLabelView(LoginRequired, ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'labels/index.html'


class CreateLabelView(SuccessMessageMixin, LoginRequired,
                      CreateView):
    model = Label
    template_name = 'labels/create.html'
    form_class = LabelCreateForm
    success_url = LABEL_INDEX

    success_message = _('Label created successfully')


class UpdateLabelView(SuccessMessageMixin, LoginRequired,
                      UpdateView):
    model = Label
    context_object_name = 'label'
    template_name = 'labels/update.html'
    form_class = LabelCreateForm
    success_url = LABEL_INDEX

    success_message = _("Label updated successfully")


class DeleteLabelView(SuccessMessageMixin, LoginRequired,
                      DeletionRestricted, DeleteView):
    model = Label
    context_object_name = 'label'
    template_name = 'labels/delete.html'
    success_url = LABEL_INDEX
    reject_url = LABEL_INDEX

    success_message = _("Label deleted successfully")
    reject_message = _('Unable to delete label because it is in use')
