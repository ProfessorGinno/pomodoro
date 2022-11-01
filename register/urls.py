from django.urls import path
from .views import register_request, homepage

urlpatterns = [
    path('register/', register_request, name="register"),
]