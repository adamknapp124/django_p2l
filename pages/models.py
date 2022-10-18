from django.db import models

# Create your models here.
class Review(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    value = models.IntegerField(null=True)
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    RATING = [
        (1, 'Below Average'),
        (2, 'I\'ve Seen Worse'),
        (3, 'Not Too Shabby'),
        (4, 'Pretty Alright'),
        (5, 'Vince McMahon')
    ]