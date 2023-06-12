# Master URL

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', include('first_app.urls')),
    path('util/', include('util.urls')),
]
