from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Game
from .forms import PostForm, GameForm
from django.utils.text import slugify

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "news/index.html"
    paginate_by = 6

class GameList(generic.ListView):
    queryset = Game.objects.all()
    template_name = "news/game_list.html"
    paginate_by = 6

def create(form):

    if form.is_valid():
        object = form.save(commit=False)
        object.slug = slugify(object.title)
        object.save()
        return object
    else:
        print(form.errors)

def post(request, slug):

    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    game = post.topic
    
    form = PostForm()

    return render(
        request,
        "news/post.html",
        {"post": post, "game": game, "form": form},
    )

def game(request, slug):

    queryset = Game.objects.all()
    game = get_object_or_404(queryset, slug=slug)
    platform = Game.PLATFORM[game.platform][1]
    posts = game.posts.all().order_by("-created_on")
    post_count = game.posts.all()
    form = GameForm()
    return render(
        request,
        "news/game.html",
        {"game": game, "posts": posts, "platform": platform, 
         "post_count": post_count, "form": form
        },
    )

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if create(form):
            messages.add_message(request, messages.SUCCESS, 'Post is created')
    form = PostForm()

    return render(
        request,
        "news/create_post.html",
        {"form": form,
        },
    )

def create_game(request):
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        if create(form):
            messages.add_message(request, messages.SUCCESS, 'Game created!')
        else:
            messages.add_message(request, messages.ERROR, 'Error creating game!')
    form = GameForm()

    return render(
        request,
        "news/create_game.html",
        {"form": form,
        },
    )

        

def post_edit(request, slug):
    """
    view to edit posts
    """
    if request.method == "POST":
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        form = PostForm(data=request.POST, instance=post)
        if create(form):
            messages.add_message(request, messages.SUCCESS, 'Post updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating post!')

    return HttpResponseRedirect(reverse('post', args=[slug]))

def game_edit(request, slug):
    """
    view to edit posts
    """
    if request.method == "POST":
        queryset = Game.objects.all()
        game = get_object_or_404(queryset, slug=slug)
        form = GameForm(request.POST, request.FILES, instance=game)
        if create(form):
            messages.add_message(request, messages.SUCCESS, 'Game updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating game!')

    return HttpResponseRedirect(reverse('game', args=[slug]))


    
def post_delete(request, slug):
    """
    view to delete comment
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    #comment = get_object_or_404(Comment, pk=comment_id)
    post.delete()
    messages.add_message(request, messages.SUCCESS, 'Post deleted!')

    return HttpResponseRedirect(reverse('home'))

def game_delete(request, slug):
    """
    view to delete game
    """
    queryset = Game.objects.all()
    game = get_object_or_404(queryset, slug=slug)
    game.delete()
    messages.add_message(request, messages.SUCCESS, 'Game deleted!')

    return HttpResponseRedirect(reverse('game_list'))
    