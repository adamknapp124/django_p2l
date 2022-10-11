from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from allauth.account.views import PasswordChangeView

from .forms import CustomUserChangeForm

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('my-account')

class MyAccountPageView(UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user