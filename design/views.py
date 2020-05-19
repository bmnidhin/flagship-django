from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from taggit.managers import TaggableManager

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'design/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # post_instance = Post.objects.get_or_create()
    post_related = Post.objects.filter(published_date__lte=timezone.now()).order_by('?')[0:3]
    return render(request, 'design/post_detail.html', {'post': post,'post_related': post_related})    
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'design/post_detail.html', {'post': post})