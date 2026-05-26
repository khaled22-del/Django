from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag


def starting_page(request):

    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):

    all_posts = Post.objects.all().order_by("-date")

    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):

    identified_post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })


def authors(request):

    all_authors = Author.objects.all()

    return render(request, "blog/author-list.html", {
        "authors": all_authors
    })


def author_detail(request, id):

    author = get_object_or_404(Author, id=id)

    return render(request, "blog/author-detail.html", {
        "author": author
    })


def tags(request):

    all_tags = Tag.objects.all()

    return render(request, "blog/tags.html", {
        "tags": all_tags
    })


def tag_posts(request, tag):

    selected_tag = get_object_or_404(Tag, caption=tag)

    posts = Post.objects.filter(tags=selected_tag)

    return render(request, "blog/tag-posts.html", {
        "tag": selected_tag,
        "posts": posts
    })