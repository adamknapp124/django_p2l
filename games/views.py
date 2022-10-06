from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class MathGameView(TemplateView):
    template_name = 'math-game.html'

class AnagramGameView(TemplateView):
    template_name = 'anagram-game.html'

