from django.contrib import admin
from blog.models import Article


@admin.register(Article)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'is_public', 'view_count')
    list_filter = ('title',)
    search_fields = ('title', 'content')
