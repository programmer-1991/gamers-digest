from django.contrib import admin
from .models import Post, Game
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug',)
    search_fields = ['title']
    #list_filter = ('',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)



# Register your models here.
admin.site.register(Game)