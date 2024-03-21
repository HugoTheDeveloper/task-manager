from django import forms
from .models import Status
from django.utils.translation import gettext_lazy as _


class CreateStatusForm(forms.ModelForm):
    class Meta():
        model = Status
        fields = ['name']
        labels = {'name': _('Name')}
