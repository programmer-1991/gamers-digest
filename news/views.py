from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post, Game
from .forms import PostForm

# Create your views here.
def create(request):
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.post = post
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post is created'
            )
    post_form = PostForm()

    return render(
        request,
        "news/create_post.html",
        {"post_form": post_form,
        },
    )
    


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
    platform = Game.PLATFORM[game.platform][1]
    posts = game.posts.all().order_by("-created_on")
    post_count = game.posts.all()
    
    return render(
        request,
        "news/game.html",
        {"game": game, "posts": posts, "platform": platform, 
         "post_count": post_count,
        },
    )
    
    