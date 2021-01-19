from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from .forms import BlogForm, TagForm
from pprint import pprint

# Create your views here.
def form(request, template_name='forms/blog_form.html', form_class=BlogForm):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogsie' : blogs})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/blogs/blogs.html', {'blogs' : blogs})

def updateBlog(request, pk):
    update = Blog.objects.get(id=pk)
    form = BlogForm(instance=update)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=update)

        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'forms/blog_form.html', {'form': form})
    # return form_update(request, template_name='forms/blog_form.html', form_class=BlogForm, update_variable=update)

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'pages/tags/tags.html', {'tags' : tags})

def createTag(request):
    return form(request, template_name='forms/blog_form.html', form_class=TagForm)

def comments(request):
    comments = Comment.objects.all()
    return render(request, 'pages/comments/comments.html', {'comments' : comments})

