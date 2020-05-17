from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

from django.views.generic import View
from django.http import HttpResponse # Add this

from .forms import ContactForm # Add this

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:3]
    return render(request, 'blog/home.html', {'posts': posts})   

def post_contact(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/about.html', {'posts': posts})

def post_me(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/about.html', {'posts': posts})
    
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
# def contact_us(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # send email code goes here
#             return HttpResponse('Thanks for contacting us!')
#     else:
#         form = ContactForm()

#     return render(request, 'blog/about.html', {'form': form})