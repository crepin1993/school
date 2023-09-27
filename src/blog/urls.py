
from django.contrib import admin
from django.urls import path

from .views import BlogIndexView, DetailActualiteView

urlpatterns = [
    path('', BlogIndexView),
    path('actualite-vue-detail/<str:slug>/', DetailActualiteView, name='blog-post')
]
