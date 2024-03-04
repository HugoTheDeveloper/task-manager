from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class StartPageView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'start_page.html', {})


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    # authentication_form = AuthenticationForm
    next_page = reverse_lazy('start_page')
    success_message = _('You are logged in successfully!')


class CustomLogoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('start_page')
    success_message = _('You are logged out')
# class CustomLoginView(View):
#
#     @staticmethod
#     def get(request, *args, **kwargs):
#         form = AuthenticationForm()
#         return render(request, 'login.html', {'form': form})


