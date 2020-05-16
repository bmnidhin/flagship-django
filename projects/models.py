
# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
   
    madeby = models.CharField(max_length=200, null = True, blank = True)
    image_link = models.CharField(max_length=200, null = True, blank = True)
    text = models.TextField( null = True, blank = True)
    short =models.TextField(max_length=400, null = True, blank = True)
    new = models.CharField(max_length=200, null = True, blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    related_one_title = models.CharField(max_length=200, null = True, blank = True)
    related_one_Photo = models.CharField(max_length=200, null = True, blank = True)
    related_one_category = models.CharField(max_length=200, null = True, blank = True)
    related_one_link = models.CharField(max_length=200, null = True, blank = True)

    related_two_title = models.CharField(max_length=20, null = True, blank = True)
    related_two_Photo = models.CharField(max_length=200, null = True, blank = True)
    related_two_category = models.CharField(max_length=200, null = True, blank = True)
    related_two_link = models.CharField(max_length=200, null = True, blank = True)

    related_three_title = models.CharField(max_length=20, null = True, blank = True)
    related_three_Photo = models.CharField(max_length=200, null = True, blank = True)
    related_three_category = models.CharField(max_length=200, null = True, blank = True)
    related_three_link = models.CharField(max_length=200, null = True, blank = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title