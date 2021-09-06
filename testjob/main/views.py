from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView

from .models import *
from .forms import PostForm, PostFormSearch


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


def findTitle(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        post = Post.objects.all()
        for p in post:
            print(p.description)
            if p.title == title:
                return HttpResponse(f"<h1>{p.title}</h1><br><p>{p.description}</p>")
            else:
                return HttpResponse("THERE IS NO POST WITH SUCH NAME, TRY AGAIN")


    form = PostFormSearch()
    context = {
        'form': form
    }
    return render(request, 'main/search.html', context)

def deletepost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts')


class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'main/edit.html'



