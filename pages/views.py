from django.contrib import messages
from .forms import ContactForm
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView


# Create your views here.
class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


class ContactForm(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('pages:thanks.html')


class HomePageView(TemplateView):
    template_name = 'pages/home.html'