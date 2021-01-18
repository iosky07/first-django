from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blogs/', views.blogs),
    path('tags/', views.tags),
]


