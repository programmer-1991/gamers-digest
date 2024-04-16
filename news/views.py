from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Game

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "news/index.html"
    paginate_by = 6

def post(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    game = post.topic
    return render(
        request,
        "news/post.html",
        {"post": post, "game": game},
    )

def game(request, slug):

    queryset = Game.objects.all()
    game = get_object_or_404(queryset, slug=slug)
    posts = game.posts.all().order_by("-created_on")
    return render(
        request,
        "news/game.html",
        {"game": game, "posts": posts},
    )