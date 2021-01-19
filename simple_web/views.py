from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import BlogForm

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogsie' : blogs})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/blogs/blogs.html', {'blogs' : blogs})

def createTag(request):
    return render(request, 'pages/tags/create.html')

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'pages/tags/tags.html', {'tags' : tags})

def createBlog(request, template_name='forms/blog_form.html', form_class=BlogForm):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

def comments(request):
    comments = Comment.objects.all()
    return render(request, 'pages/comments/comments.html', {'comments' : comments})

