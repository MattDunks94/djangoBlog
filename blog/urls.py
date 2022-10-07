from . import views
from django.urls import path


urlpatterns = [
    # Path to our PostList view, with template being 'index.html'.
    path('', views.PostList.as_view(), name='home')
]