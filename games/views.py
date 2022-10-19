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
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')[:10]
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')[:10]
        return context


class MathGameView(TemplateView):
    template_name = 'math-game.html'


def record_score(request):
    data = json.loads(request.body)
    game = data['game']
    if game == 'MATH':
        user_name = request.user
        score = data['score']
        operation = data['operation']
        max_number = data['maxNumber']
        new_score = GameScore(user_name=user_name, game=game, score=score,
                    operation=operation, max_number=max_number)
    else:
        user_name = request.user
        score = data['score']
        word_length = data['word_length']
        new_score = GameScore(user_name=user_name, game=game, score=score,
                    word_length=word_length)

    new_score.save()

    response = {
        'success': True
    }

    return JsonResponse(response)