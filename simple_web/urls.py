from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blogs/', views.blogs, name="blog"),
    path('blogs/create/', views.form, name="form"),
    path('blogs/update/<str:pk>/', views.updateBlog, name="update-blog"),
    path('tags/', views.tags, name="tag"),
    path('tags/create/', views.createTag, name="create-tag"),
    path('comments/', views.comments, name="comment"),
]
