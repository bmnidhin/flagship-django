from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_home, name='post_home'),
    path('me', views.post_me, name='post_me'),
    path('contact', views.post_contact, name='post_contact'),
    path('myaccount', views.post_account, name='post_account'),
    path('blog', views.post_list, name='post_list'),
    path('blog/<slug>/', views.post_detail, name='post_detail'),
    path('blog/<slug>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
#    path('posts/<slug:slug>', views.post_detail, name='post_detail')
]