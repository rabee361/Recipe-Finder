from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('contact/' , contact , name="contact"),
    path('index/' , index, name="index"),
    path('blog/' , ListBlogs.as_view() , name="blog"),
    path('recipes/' , test , name="test"),
    path('single-blog/<str:pk>', single_blog , name="single-blog"),
    path('about/' , about , name="about"),
    path('test/' , test , name="test"),
    path('stream-text-file/', stream_large_text_file, name='stream_text_file'),
]

 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)