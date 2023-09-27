
from django.contrib import admin
from django.urls import path

from .views import index,send_email

urlpatterns = [
    path('', index),
    path('post-email/', send_email, name="send-email")
]
