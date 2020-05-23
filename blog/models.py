

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from datetime import datetime, timedelta

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    # headshot = models.ImageField(null=True, blank=True, upload_to="images/")
    image_link = models.CharField(max_length=200, null = True, blank = True)
    caption = models.CharField(max_length=400, null = True, blank = True)
    short = models.CharField(max_length=400, null = True, blank = True)
    text = models.TextField()

    tags = TaggableManager(verbose_name="Tags", help_text="A comma-separated list of tags.", through=None, blank=False,related_name='blotags')

    button_text = models.CharField(max_length=200, null = True, blank = True)
    button_link = models.CharField(max_length=200, null = True, blank = True)



    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
     

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100,)
    avathar = models.CharField(max_length=400, null = True, blank = True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.text 

      
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    # def author(self, request, obj, form, change):
    #     obj.author = request.user
    #     super().author(request, obj, form, change)
    #     exclude = ['author',]

# def pre_save_receiver(sender, instance, *args, **kwargs): 
#    if not instance.slug: 
#        instance.slug = unique_slug_generator(instance) 
  
  
# pre_save.connect(pre_save_receiver, sender = Post) 



