
from django.contrib import admin
from django.urls import path

from .views import index, DetailFormationView


urlpatterns = [
    path('', index),
    path('formation-vue-detail/<str:slug>/', DetailFormationView, name='formation-detail')
]
