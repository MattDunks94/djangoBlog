from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Indicates the status of the post created by user.
STATUS = ((0, 'Draft'), (1, 'Published'))

# Create your models here.


# Model for user posts. 
class Post(models.Model):
    # Title of post. 
    title = models.CharField(max_length=200, unique=True)
    # Slug is like a label, identifies part of a web address, end of URL.
    slug = models.SlugField(max_length=200, unique=True)
    # The author of the post created, this being the user.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
    # Updates date to time/date when post is updated.
    updates_on = models.DateTimeField(auto_now=True)
    # Content of post, text.
    content = models.TextField()
    # Images featured within the post.
    # First parameter is type, second is a placeholder.
    featured_image = CloudinaryField('image', default='placeholder')
    # Excerpt is a 'snippet' of a post instead of all content.
    excerpt = models.TextField(blank=True)
    # Date for when post is created on.
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # ManytoManyField refers to multiple instances from a model.
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


# Model for comments.
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
        )
    # Name field.
    name = models.CharField(max_length=80)
    # Email field.
    email = models.EmailField()
    # Body field, contains main comment content.
    body = models.TextField()
    # Date created on.
    created_on = models.DateTimeField(auto_now_add=True)
    # Approved checkbox, default as False(empty).
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"