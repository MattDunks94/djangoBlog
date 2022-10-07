from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # Filter posts by published ones only.
        queryset = Post.objects.filter(status=1)
        # Collects published post with correct slug.
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            
