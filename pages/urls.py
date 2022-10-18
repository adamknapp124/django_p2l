from django.urls import path
from . import views

from .views import AboutUsView, HomePageView, ReviewPageView, user_review

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact/', views.contact, name='contact'),
    path('review/', ReviewPageView.as_view(), name="review"),
    path('review/record-review', user_review, name='user_review'),
    path('record-review/', user_review, name='user_review'),
]