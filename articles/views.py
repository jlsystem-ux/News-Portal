"""
Views for listing and displaying news articles.
"""

from articles.models import Article
from django.shortcuts import render, get_object_or_404


# View to list articles
def article_list_view(request):
    """Display a list of all articles, ordered by publish date (newest first)."""
    # You can filter by status='published' later, for now let's get all
    # articles_queryset = Article.objects.filter(status='published').order_by('-publish_date')
    articles_queryset = Article.objects.all().order_by('-publish_date')  # Get all articles, newest first

    context = {
        'articles': articles_queryset,
    }
    # This will look for a template at: articles/templates/articles/article_list.html
    return render(request, 'articles/article_list.html', context)


# View to display a single article detail
def article_detail_view(request, article_slug):  # 'article_slug' comes from the URL pattern
    """Display the details of a single article identified by its slug."""
    # article = get_object_or_404(Article, slug=article_slug, status='published')
    # For now, let's get by slug only for testing
    article = get_object_or_404(Article, slug=article_slug)

    context = {
        'article': article,
    }
    # This will look for a template at: articles/templates/articles/article_detail.html
    return render(request, 'articles/article_detail.html', context)


# View to render the home page
def home_view(request):
    """Render the home page template."""
    return render(request, 'home.html')
