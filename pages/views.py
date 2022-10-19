import json
from django.http import JsonResponse

from .forms import ContactForm
from .models import Review

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


class ReviewPageView(TemplateView):
    template_name = 'review_form.html'


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

def user_review(request):
    data = json.loads(request.body)
    print(request.user)

    first_name = data['fname']
    last_name = data['lname']
    email = data['email']
    review = data['review']
    rating = data['value']

    new_score = Review(first_name=first_name, last_name=last_name, email=email, review=review, rating=rating)
    new_score.save()

    response = {
        'success': True
    }

    return JsonResponse(response) 