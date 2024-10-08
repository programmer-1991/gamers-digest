from .models import Post, Game
from django import forms


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'genre', 'description', 'platform', 'age_rating',
                  'developer', 'publisher', 'release', 'featured_image')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'topic', 'intro', 'featured_image', 'content')
