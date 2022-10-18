import json
from django.http import JsonResponse

from django.views.generic import TemplateView

from .models import GameScore


# Create your views here.
class AnagramGameView(TemplateView):
    template_name = 'anagram-game.html'


class GameScoresView(TemplateView):
    template_name = 'game-scores.html'

    def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context


class MathGameView(TemplateView):
    template_name = 'math-game.html'


def record_score(request):
    data = json.loads(request.body)
    print(request.user)

    user_name = request.user
    game = data['game']
    score = data['score']

    new_score = GameScore(user_name=user_name, game=game, score=score)
    new_score.save()

    response = {
        'success': True
    }

    return JsonResponse(response)