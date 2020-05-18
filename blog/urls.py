from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_home, name='post_home'),
    path('me', views.post_me, name='post_me'),
    path('contact', views.post_contact, name='post_contact'),
    path('blog', views.post_list, name='post_list'),
    path('blog/<slug>/', views.post_detail, name='post_detail'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
#    path('posts/<slug:slug>', views.post_detail, name='post_detail')
]