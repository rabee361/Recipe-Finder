from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('all-recipes/' , All_Recipes3.as_view() , name="all-recipes"),
    path('v2/all-recipes/' , All_Recipes2.as_view() , name="all-recipes2"),
    # path('detail-recipe/<str:pk>' , Detail_Recipe.as_view() , name="detail-recipe")
    path('blogs/' , GetBlogs.as_view() , name="blogs"),
    path('blog/<str:pk>' , GetSingleBlog.as_view() , name="single-blog"),
    path('write-message/' , CreateMessage.as_view() , name="create-msg"),
    path('gallery/' , GalleryImages.as_view() , name="gallery")
]
