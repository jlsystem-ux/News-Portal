from django.contrib import admin
from .models import Article
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish_date', 'status')
    list_filter = ('status', 'created_at', 'publish_date', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)} # Automatically generates slug from title
    raw_id_fields = ('author',) # Better UI for selecting author if you have many users
    date_hierarchy = 'publish_date'
    ordering = ('status', '-publish_date')