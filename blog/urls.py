from . import views
from django.urls import path


urlpatterns = [
    # Path to our PostList view, with template being 'index.html'.
    path('', views.PostList.as_view(), name='home'),
    # <slug:slug>/ captures URL value, in this case the slug value.
    # First slug is the path convertor, second is a keyword.
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]