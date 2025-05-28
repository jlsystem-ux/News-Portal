"""
URL configuration for the articles app.
"""

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list_view, name='article_list'),
    path('<slug:article_slug>/', views.article_detail_view, name='article_detail'),
]
