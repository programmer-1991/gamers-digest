from django.test import TestCase
from .forms import PostForm
from .models import Post, Game



class TestPostForm(TestCase):

    def test_form_is_valid(self):
        game = Game.objects.create(title='a game',release="2024-05-31")
        post_form = PostForm({'title' : 'my post', 'topic' : game, 'intro': 'new intro', 'content' : 'This is a great post'})
        print(post_form.errors)
        self.assertTrue(post_form.is_valid(), msg="Form is not valid")
        
    def test_form_is_invalid(self):
        game = Game.objects.create(title= 'a game',release= "2024-05-31")
        post_form = PostForm({'title' : '', 'topic' : game, 'intro': 'new intro', 'content' : ''})
        self.assertFalse(post_form.is_valid(), msg="Form is valid")
        
        
