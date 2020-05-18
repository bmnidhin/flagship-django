from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='project_list'),
    path('<slug>/', views.post_detail, name='project_detail'),
]