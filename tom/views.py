from django.shortcuts import render
from django.utils import timezone
# from .models import Post
from django.shortcuts import render, get_object_or_404

from django.views.generic import View
from django.http import HttpResponse # Add this

# from .forms import ContactForm # Add this
from taggit.managers import TaggableManager
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.shortcuts import redirect

    #
 
def post_tom(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        # f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/accounts/login')
 
    else:
        # f = UserCreationForm()
        f = CustomUserCreationForm()
    return render(request, 'registration/register.html',{'form': f}) 
