from django.shortcuts import render
from django.utils import timezone
from .forms import PostForm, CommentForm
from .models import Post,Comment
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from django.views.generic import View
from django.http import HttpResponse # Add this
import allauth.app_settings
from allauth.account.models import EmailAddress
from allauth.account.utils import get_next_redirect_url, setup_user_email


# from .forms import ContactForm # Add this
from taggit.managers import TaggableManager
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect




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
    
    
@login_required
def post_account(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/myaccount.html', {'posts': posts})
    
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
def add_comment_to_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.avathar= request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
        return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)






def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # post_instance = Post.objects.get_or_create()
    post_related = Post.objects.filter(published_date__lte=timezone.now()).order_by('?')[0:3]
    return render(request, 'blog/post_detail.html', {'post': post,'post_related': post_related})

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

