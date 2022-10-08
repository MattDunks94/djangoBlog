from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm

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
        # Filters approved comments only, in ascending order.
        # This displays conversations, with oldest comment first.
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        # Checks whether logged in user has liked a post.
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # Renders post details to post_detail.html file.
        return render(
            request, "post_detail.html",
            {
                "post": post,
                "comments": comments,
                # This tells user comment is awaiting approval.
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # This collects our posted form data.
        comment_form = CommentForm(data=request.POST)
        # Checking if form is completed, valid.
        if comment_form.is_valid():
            # Requesting users email and username.
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            # Calling save method on our posted form. Not saving to DB.
            comment = comment_form.save(commit=False)
            # Assigning a post to the comment made.
            # This tells us which post the comment has been left on.
            comment.post = post
            # Saving the comment form in the DB. 
            comment.save()
        # If form is invalid, returns empty form. 
        else:
            comment_form = CommentForm()

        # Renders post details to post_detail.html file.
        return render(
            request, "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
