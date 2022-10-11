from django.contrib import messages
from .forms import ContactForm
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView


# Create your views here.
class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

    def get(self, request, *args, **kwargs):
        messages.debug(request, 'Debug message.')
        messages.info(request, 'Info message.')
        messages.success(request, 'Success message.')
        messages.warning(request, 'Warning message.')
        messages.error(request, 'Error message.')
        return super().get(request, args, kwargs)


class ContactForm(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('pages:thanks.html')


class HomePageView(TemplateView):
    template_name = 'pages/home.html'