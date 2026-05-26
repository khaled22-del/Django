from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag


def starting_page(request):
    """
    Mostra la pàgina principal amb els 3 darrers posts.
    """

    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    """
    Mostra tots els posts ordenats per data descendent.
    """

    all_posts = Post.objects.all().order_by("-date")

    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    """
    Mostra el detall d'un post concret utilitzant el slug.
    """

    identified_post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })


def authors(request):
    """
    Mostra el llistat de tots els autors.
    """

    all_authors = Author.objects.all()

    return render(request, "blog/author-list.html", {
        "authors": all_authors
    })


def author_detail(request, id):
    """
    Mostra el detall d'un autor i els seus posts.
    """

    author = get_object_or_404(Author, id=id)

    return render(request, "blog/author-detail.html", {
        "author": author
    })


def tags(request):
    """
    Mostra totes les tags disponibles.
    """

    all_tags = Tag.objects.all()

    return render(request, "blog/tags.html", {
        "tags": all_tags
    })


def tag_posts(request, tag):
    """
    Mostra tots els posts relacionats amb una tag concreta.
    """

    selected_tag = get_object_or_404(Tag, caption=tag)

    posts = Post.objects.filter(tags=selected_tag)

    return render(request, "blog/tag-posts.html", {
        "tag": selected_tag,
        "posts": posts
    })