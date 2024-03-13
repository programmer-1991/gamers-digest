from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "draft"), (1, "published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "news_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank = True)
    class Meta:
        ordering = ["-created_on"]