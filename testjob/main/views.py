from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView

from .models import *
from .forms import PostForm


def index(request):
    return render(request, 'main/index.html')


def posts(request):

    posts = Post.objects.all()
    context = {
        'title': 'post',
        'posts': posts
    }
    return render(request, 'main/posts.html', context)


def addpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')

    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'main/addpost.html', context)


def deletepost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts')


class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'main/edit.html'


