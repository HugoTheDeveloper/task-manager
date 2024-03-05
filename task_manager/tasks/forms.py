from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Task


class CreateTaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'label_set']

        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'label_set': _('Labels')
        }
        status = forms.ChoiceField(initial='---------',
                                   widget=forms.Select(
                                       attrs={
                                           'required': True,
                                           'size': 2,
                                       }
                                   ))
        executor = forms.ChoiceField(initial='---------',
                                     widget=forms.Select(
                                         attrs={'size': 10}
                                     ))
        label_set = forms.MultipleChoiceField()
