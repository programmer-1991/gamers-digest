from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=32, unique=True)
    genre = models.CharField(max_length=32)
    developer = models.CharField(max_length=32)
    publisher = models.CharField(max_length=32)
    release = models.DateField()
    def __str__(self):
        return f"{self.title}"

class Post(models.Model):
    title = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True)
    content = models.TextField()
    topic = models.ForeignKey(Game, on_delete = models.CASCADE, related_name = "news_posts", default=1)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title}"
