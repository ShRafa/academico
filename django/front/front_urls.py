from django.urls import path
from . import front_views

urlpatterns = [
    path('', front_views.home),
]