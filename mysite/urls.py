
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include
from django.conf.urls.static import static # new
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', include('tom.urls')),
    path('accounts/social', include('allauth.urls')),
    path('articles/comments/', include('django_comments.urls')),
    path('summernote/', include('django_summernote.urls')),
    # path('accounts/login/', views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('projects/', include('projects.urls')),
    path('design/', include('design.urls')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)