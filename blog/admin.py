from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Comment)

admin.site.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'pub_date')
    search_fields = ['title', 'content']
    list_filter = ('status', 'pub_date')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

