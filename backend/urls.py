from django.contrib import admin
from django.urls import path
from blog.views import BlogPostList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', BlogPostList.as_view()),
]
