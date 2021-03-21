from django.urls import path
from .views import PostDetailView, PostListView, PostCreate
from . import views


app_name = 'posts'

urlpatterns = [
    path('posts/create/', PostCreate.as_view(), name="post_create"),
    path('', PostListView.as_view(), name='list'),
    path('posts/home/', PostListView.as_view(), name='list2'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='detail'),

    #path('', views.home, name='home')
]