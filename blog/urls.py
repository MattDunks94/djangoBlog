from . import views
from django.urls import path


urlpatterns = [
    # Path to our PostList view, with template being 'index.html'.
    path('', views.PostList.as_view(), name='home'),
    # Path to PostDetail view, from views.py.
    # <slug:slug>/ captures URL value, in this case the slug value.
    # First slug is the path convertor, second is a keyword.
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # Path to PostLike view, from views.py.
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')
]