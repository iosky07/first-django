from django.forms import ModelForm
from .models import *

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'