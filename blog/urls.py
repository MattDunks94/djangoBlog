from . import urls
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home')
]