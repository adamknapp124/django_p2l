from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    # Admin
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

    # Favicon
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('image/favicon.ico'))),

    # Local Apps
    path('', include('pages.urls')),
    path('account/', include('users.urls')),
    path('', include('games.urls')),

    # User Management
    path('account/', include('users.urls')),
    path('account/', include('allauth.urls')),
]
