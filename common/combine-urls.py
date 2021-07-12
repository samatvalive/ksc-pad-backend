from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('launchpad/', include('api.urls.launchpad-urls')),
]
