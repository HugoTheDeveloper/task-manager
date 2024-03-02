from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect


class AccessChangeAccountMixin(UserPassesTestMixin):
    def test_func(self):
        user_id_to_change = self.kwargs.get('pk') # noqa
        return self.request.user.pk == user_id_to_change # noqa

    def handle_no_permission(self):
        message_txt = _("You haven't permission to edit or delete this user!")
        messages.error(self.request, message_txt) # noqa
        return redirect('users_index')
