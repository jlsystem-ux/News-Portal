"""
Django app for managing and displaying news articles.
"""

# news/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Optional: if you want to link articles to authors


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish_date')  # For SEO-friendly URLs
    # Optional: Link to a User model if you have authors
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # Or models.SET_NULL, null=True, blank=True if an article can exist without an author
        related_name='news_articles',
        null=True,  # Allow articles to not have an author initially or if user is deleted
        blank=True
    )
    content = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the object is first created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set every time the object is saved

    # Status for drafts/published articles (optional but common)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # Optional: An image for the article
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # Requires Pillow library

    class Meta:
        ordering = ('-publish_date',)  # Default ordering for queries: newest first

    def __str__(self):
        return self.title

    # Optional: A method to get the absolute URL for an article (useful for templates)
    # from django.urls import reverse
    # def get_absolute_url(self):
    #     return reverse('news:article_detail', args=[self.slug]) # Assumes you have a URL pattern named 'article_detail'