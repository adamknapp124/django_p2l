from django.db import models
from django.urls import reverse

from common.utils.text import unique_slug

# Create your models here.
class GameScore(models.Model):

    MATH = 'MATH'
    ANAGRAM = 'ANAGRAM'

    GAME_CHOICES = [
        (MATH, 'Math Game'),
        {ANAGRAM, 'Anagram Game'}
    ]

    user_name = models.TextField()
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    operation = models.TextField(null=True, blank=True)
    max_number = models.IntegerField(null=True)
    word_length = models.IntegerField(blank=True, null=True)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    