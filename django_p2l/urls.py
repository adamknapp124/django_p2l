from django.contrib import admin
from django.urls import path, include
from games.views import HomeView

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('games.urls')),
]
