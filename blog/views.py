from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
    
    
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

# def detale_bajki(request, slug):
#     detale_bajki = get_object_or_404(Wpisy, slug=slug)
# def post_detail(request, slug):
#     post= Post.objects.filter(slug__iexact = slug)
#     return render(request, 'blog/post_detail.html',  {'post': post})

# def post_detail(request, slug): 
#     q = Post.objects.filter(slug__iexact = slug) 
#    if q.exists(): 
#        q = q.first() 
#    else: 
#        return HttpResponse('<h1>Post Not Found</h1>') 
#    context = { 
  
#        'post': q 
#    } 
#    return render(request, 'blog/post_detail.html', context)
