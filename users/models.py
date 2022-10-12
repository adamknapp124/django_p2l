from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.db import models
from django.urls import reverse

def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 200 or h > 200:
        raise ValidationError('Avatar must be no bigger than 200x200 pixels.')

class CustomUser(AbstractUser):
    user_name = models.TextField(null=True)
    dob = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )
    
    def get_absolute_url(self):
        return reverse('my-account')