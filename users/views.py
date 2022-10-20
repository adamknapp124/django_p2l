from django.shortcuts import render

# Create your views here.
from allauth.account.views import PasswordChangeView

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView

from games.models import GameScore
from .forms import CustomUserChangeForm

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('my-account')

class MyAccountPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user


class MyScoresPage(TemplateView):
    template_name = 'account/my_scores.html'

    def get_context_data(self, **kwargs):
        context = super(MyScoresPage, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')[:10]
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')[:10]
        return context

    def get_object(self):
        return self.request.user