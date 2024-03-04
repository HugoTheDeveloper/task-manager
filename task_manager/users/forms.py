from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _


class CreateUserForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput, help_text=_('Please enter your password again to confirm.'))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if len(password) < 8:
            self.add_error('password', 'Password too short!')
        if password != password_confirm:
            self.add_error('password_confirm', 'Passwords do not match!')
        return cleaned_data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password',
                  'password_confirm']

        labels = {
            'first_name': _('Name'),
            'last_name': _('Sirname'),
            'username': _('Username'),
            'password': _('Password')
        }
        help_texts = {
            'username': _('Required field. No more than '
                          '150 characters. Only letters, numbers and '
                          '@/./+/-//_ symbols.'),
            'password': _('Your password must contain at least 8 characters.')
        }
