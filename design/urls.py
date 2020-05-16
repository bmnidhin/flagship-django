from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='design_list'),
    path('post/<slug>/', views.post_detail, name='design_detail'),
]