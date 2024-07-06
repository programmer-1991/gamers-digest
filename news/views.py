from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Game
from .forms import PostForm
from django.utils.text import slugify

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "news/index.html"
    paginate_by = 6

def create(request):
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.slug = slugify(post.title)
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

def post_edit(request, slug):
    """
    view to edit posts
    """
    if request.method == "POST":
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        form = PostForm(data=request.POST, instance=post)
        
        if form.is_valid():
            post = form.save(commit=False)
            #post.game = game
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Post updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating post!')

    return HttpResponseRedirect(reverse('post', args=[slug]))

def post(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    game = post.topic
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post is created'
            )
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
    
    return render(
        request,
        "news/game.html",
        {"game": game, "posts": posts, "platform": platform, 
         "post_count": post_count,
        },
    )
    
    