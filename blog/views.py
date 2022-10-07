from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


# View for Post List.
class PostList(generic.ListView):
    model = Post
    # Collects Post keys, filters published(1) posts in descending order.
    # Post status (0) is draft (1) is published.
    # Add '-' to created_on to view posts in descending order.
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # Paginate means seaperate into pages.
    # Here, we are limiting the amount of posts displayed to 6.
    # If posts go beyond 6, Django adds automated page navigation. 
    paginate_by = 6
