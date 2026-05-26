from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse


class Author(models.Model):
    """
    Model que representa els autors del blog.
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def post_count(self):
        """
        Retorna el nombre total de posts publicats per l'autor.
        """
        return self.posts.count()

    def __str__(self):
        """
        Retorna el nom complet de l'autor.
        """
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    """
    Model utilitzat per categoritzar els posts.
    """

    caption = models.CharField(max_length=20)

    def __str__(self):
        """
        Retorna el nom de la tag.
        """
        return self.caption


class Post(models.Model):
    """
    Model que representa els posts del blog.
    """

    title = models.CharField(max_length=150)

    excerpt = models.CharField(max_length=300)

    image_name = models.CharField(max_length=100)

    slug = models.SlugField(unique=True)

    content = models.TextField(
        validators=[MinLengthValidator(10)]
    )

    date = models.DateField(auto_now_add=True)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        """
        Genera automàticament la URL del detall del post.
        """
        return reverse("posts-detail-page", args=[self.slug])

    def __str__(self):
        """
        Retorna el títol del post.
        """
        return self.title