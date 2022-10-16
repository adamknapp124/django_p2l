from .forms import ContactForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'aknapp124@gmail.com', ['aknapp124@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return render(request, "pages/thanks.html")
      
	form = ContactForm()
	return render(request, "pages/contact.html", {'form':form})


class HomePageView(TemplateView):
    template_name = 'pages/home.html'