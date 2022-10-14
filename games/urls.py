from django.urls import path, include

from games.views import MathGameView, AnagramGameView, GameScoresView, record_score

app_name = 'games'
urlpatterns = [
    path('math-game/', MathGameView.as_view(), name='math-game'),
    path('anagram-game/', AnagramGameView.as_view(), name='anagram-game'),
    path('math-game/record-score/', record_score, name='record_score'),
    path('record-score/', record_score, name='record_score'),
    path('game-scores/', GameScoresView.as_view(), name='game-scores'),
]