from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('posts', views.posts, name='posts'),
    path('addpost', views.addpost, name='addpost'),
    path('delete/<post_id>', views.deletepost, name='delete'),
    path('edit/<int:pk>', EditPost.as_view(), name='edit'),
    path('search', views.findTitle, name='search')
]
