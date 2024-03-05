from django.db import models
from django.contrib.auth.models import user

STATUS = ((0, "draft"), (1, "published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_names = "news_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(choices=STATUS, default=0)
