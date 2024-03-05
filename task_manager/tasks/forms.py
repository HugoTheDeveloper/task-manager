from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import User


class CreateTaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields = ['name', 'description', 'status', 'executor']

        status_choices = [(status.id, status.name) for status in Status.objects.all()] # noqa
        executor_choices = [(user.pk, user.full_name) for user in User.objects.all()]

        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor')
        }
        status = forms.ChoiceField(choices=status_choices,
                                   initial='---------',
                                   widget=forms.Select(
                                       attrs={
                                           'required': True,
                                           'size': 2,
                                       }
                                   ))
        executor = forms.ChoiceField(choices=executor_choices,
                                     initial='---------',
                                     widget=forms.Select(
                                         attrs={'size': 10}
                                     ))
