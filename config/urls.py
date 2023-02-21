"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from page.views import home_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view,name= 'home_view'),
    path("user/", include("user_profile.urls", namespace="user")),
   # BLOG:
    path('blog/', include('blog.urls', namespace='blog')),

    # READ
    path('read/', include('read.urls', namespace='read')),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
