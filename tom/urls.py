from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_tom, name='post_tom'),
]