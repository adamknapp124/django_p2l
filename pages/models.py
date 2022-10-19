from django.db import models

# Create your models here.
class Review(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    rating = models.IntegerField(null=True)
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
