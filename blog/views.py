from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth.models import User
#from blog.urls import views

# Create your views here.

def posts(request):
    posts = Post.objects.all()
    context_dict = {'posts': posts}
    return render(request, 'blog/posts.html', context_dict)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts')
    else:     
        form = PostForm()
    
    context_dict = {'form': form}
    return render(request, 'blog/post_edit.html', context_dict)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
