from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import MathGameView, AnagramGameView, GameScoresView, record_score

app_name = 'games'
urlpatterns = [
    path('math-game/', login_required(MathGameView.as_view()), name='math-game'),
    path('anagram-game/', login_required(AnagramGameView.as_view()), name='anagram-game'),
    path('record-score/', record_score, name='record_score'),
    path('game-scores/', GameScoresView.as_view(), name='game-scores'),
]