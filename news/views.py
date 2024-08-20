from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Game
from .forms import PostForm, GameForm
from django.utils.text import slugify

# Create your views here.

class PostList(generic.ListView):
    """
    Returns all published posts in :model:`news.Post`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All instances of :model:`news.Post`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`news/index.html`
    """
    queryset = Post.objects.all()
    template_name = "news/index.html"
    paginate_by = 6

class GameList(generic.ListView):
    """
    Returns all games in :model:`news.Game`
    and displays them in a page of six games.
    **Context**

    ``queryset``
        All instances of :model:`news.Game`
    ``paginate_by``
        Number of games per page.

    **Template:**

    :template:`news/game_list.html`
    """
    queryset = Game.objects.all()
    template_name = "news/game_list.html"
    paginate_by = 6

def create(form):
    """
    Takes in an argument, if it's valid then it's converted 
    from a modelform to a model object and then sent to the
    database.
    **Context**

    ``form``
        a modelform object.
    ``object``
        a converted model object.
    """
    if form.is_valid():
        object = form.save(commit=False)
        object.slug = slugify(object.title)
        object.save()
        return object
    else:
        print(form.errors)

def post(request, slug):
    """
    Display an individual :model:`news.Post`.

    **Context**

    ``post``
        An instance of :model:`news.Post`.

    ``form``
        An instance of :form:`news.PostForm`
    
    ``game``
        the topic that the post is about

    **Template:**

    :template:`blog/post.html`
    """
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
    """
    Display an individual :model:`news.Game`.

    **Context**

    ``game``
        An instance of :model:`news.Game`.
    ``posts``
        All posts related to the game.
    ``post_count``
        A count of posts related to the game.
    ``form``
        An instance of :form:`news.GameForm`

    **Template:**

    :template:`blog/game.html`
    """
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
    """
    Create an individual post.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    ``form``
        An instance of :form:`news.PostForm`
    
    **Template:**

    :template:`news/create_post.html`
    """
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
    """
    Create an individual game.

    **Context**

    ``game``
        An instance of :model:`news.Game`.

    ``form``
        An instance of :form:`news.GameForm`
    
    **Template:**

    :template:`news/create_game.html`
    """
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
    Display an individual post for edit.

    **Context**

    ``post``
        An instance of :model:`news.Post`.
    ``form``
        An instance of :form:`news.PostForm`
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
    Display an individual game for edit.

    **Context**

    ``post``
        An instance of :model:`news.Game`.
    ``form``
        An instance of :form:`news.GameForm`
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
    Delete an individual post.

    **Context**

    ``post``
        An instance of :model:`news.Post`.
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    #comment = get_object_or_404(Comment, pk=comment_id)
    post.delete()
    messages.add_message(request, messages.SUCCESS, 'Post deleted!')

    return HttpResponseRedirect(reverse('home'))

def game_delete(request, slug):
    """
    Delete an individual game.

    **Context**

    ``game``
        An instance of :model:`news.Game`.
    """
    queryset = Game.objects.all()
    game = get_object_or_404(queryset, slug=slug)
    game.delete()
    messages.add_message(request, messages.SUCCESS, 'Game deleted!')

    return HttpResponseRedirect(reverse('game_list'))
    