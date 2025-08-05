from django.shortcuts import render

def post_list(request):
    return render(request, 'livemusic/post_list.html', {})
