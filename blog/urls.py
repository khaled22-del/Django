from django.urls import path
from . import views
"""
Arxiu de rutes del blog.
Defineix totes les URLs del projecte.
"""
urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.post_detail, name='posts-detail-page'),

    path('authors', views.authors, name='authors-page'),
    path('authors/<int:id>', views.author_detail, name='author-detail-page'),

    path('tags', views.tags, name='tags-page'),
    path('tags/<slug:tag>', views.tag_posts, name='tag-posts-page'),
]