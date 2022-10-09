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
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

class Game(models.Model):
    game_name = models.TextField(max_length=200)
    high_score = models.IntegerField()
    last_played = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=True, editable=False
    )

    def get_absolute_url(self):
        return reverse('games:detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.game_name