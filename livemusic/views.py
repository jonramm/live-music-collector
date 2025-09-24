from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, MusicVenue
from .forms import PostForm, MusicVenueForm

"""Posts"""

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

"""Venues"""

def venue_list(request):
    venues = MusicVenue.objects.order_by('name')
    return render(request, 'livemusic/venue_list.html', {'venues': venues})

def venue_new(request):
    if request.method == "POST":
        form = MusicVenueForm(request.POST)
        if form.is_valid():
            venue = create_and_save_venue(form, request)
            return redirect('venue_detail', pk=venue.pk)
    else:
        form = MusicVenueForm()
    return render(request, 'livemusic/venue_edit.html', {'form': form})

def venue_edit(request, pk):
    venue = get_object_or_404(MusicVenue, pk=pk)
    if request.method == "POST":
        form = MusicVenueForm(request.POST, instance=venue)
        if form.is_valid():
            venue = create_and_save_venue(form, request)
            return redirect('venue_detail', pk=venue.pk)
    else:
        form = MusicVenueForm(instance=venue)
    return render(request, 'livemusic/venue_edit.html', {'form': form})

def venue_detail(request, pk):
    venue = get_object_or_404(MusicVenue, pk=pk)
    return render(request, 'livemusic/venue_detail.html', {'venue': venue})

def create_and_save_venue(form, request):
    venue = form.save(commit=False)
    venue.created_by = request.user
    venue.created_date = timezone.now()
    venue.save()
    return venue

