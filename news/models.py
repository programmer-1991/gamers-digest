from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True)
    intro = models.CharField(max_length=1024, blank=True)
    content = models.TextField()
    topic = models.ForeignKey(Game, on_delete = models.CASCADE, related_name = "posts", default=0)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title}"

class Game(models.Model):
    PLATFORM = ((0, ""), (1, "Xbox"), (2, "Playstation"), (3, "Nintendo"), (4, "Windows"))
    title = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, null=True)
    genre = models.CharField(max_length=64)
    description = models.TextField(max_length=8192, null=True)
    platform = models.IntegerField(choices = PLATFORM, default=0)
    age_rating = models.IntegerField(null=True)
    developer = models.CharField(max_length=32)
    publisher = models.CharField(max_length=32)
    release = models.DateField()
    featured_image = CloudinaryField('image', default='placeholder')
    def __str__(self):
        return f"{self.title}"


