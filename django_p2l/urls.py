from django.contrib import admin
from django.urls import path, include
from games.views import HomeView

urlpatterns = [
    path('', include('games.urls')),
    path('admin/', admin.site.urls),
]
