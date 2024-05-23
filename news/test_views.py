from django.urls import reverse
from django.test import TestCase
from .forms import PostForm
from .models import Post, Game

class TestPostViews(TestCase):

    def setUp(self):
        self.game = Game.objects.create(title='a game', slug='a-game', release="2024-05-31")
        self.post = Post.objects.create(title="News title", slug="news-title", topic=self.game, content="News content")

    def test_render_post_page_with_post_form(self):
        response = self.client.get(reverse('post', args=['news-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"News title", response.content)
        self.assertIn(b"News content", response.content)
        self.assertIsInstance(response.context['form'], PostForm)
        
    def test_render_game_page(self):
        response = self.client.get(reverse('game', args=['a-game']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"a game", response.content)
        self.assertIn(b"May 31, 2024", response.content)
        
    def test_render_create_page(self):        
        response = self.client.get(reverse('create', args=[]))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['post_form'], PostForm)
        