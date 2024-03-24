from django.shortcuts import render
from django.views import genric
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    model = Post


