from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

        labels = {
            'first_name': _('Name'),
            'last_name': _('Sirname'),
            'username': _('Username'),
            'password': _('Password')
        }
        help_texts = {
            'username': _('Required field. No more than '
                          '150 characters. Only letters, numbers and '
                          '@/./+/-//_ symbols.')
        }
