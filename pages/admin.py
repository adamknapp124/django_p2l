from django.contrib import admin

from .models import Review

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['first_name', 'last_name', 'review']