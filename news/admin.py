from django.contrib import admin
from .models import Post, Game
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'topic', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)



# Register your models here.
@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'platform', 'release')
    search_fields = ['title', '']
    list_filter = ('platform',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)
