from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'livemusic/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'livemusic/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = create_and_save_post(form,)
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'livemusic/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = create_and_save_post(form, request)
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'livemusic/post_edit.html', {'form': form})

def create_and_save_post(form, request):
    post = form.save(commit=False)
    post.author = request.user
    post.published_date = timezone.now()
    post.save()
    return post
