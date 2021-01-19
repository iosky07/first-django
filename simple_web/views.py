from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogsie' : blogs})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/blogs/blogs.html', {'blogs' : blogs})

def createBlog(request):
    return render(request, 'pages/blogs/create.html')

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'pages/tags/tags.html', {'tags' : tags})

def createTag(request):
    return render(request, 'pages/tags/create.html')

def comments(request):
    comments = Comment.objects.all()
    return render(request, 'pages/comments/comments.html', {'comments' : comments})

