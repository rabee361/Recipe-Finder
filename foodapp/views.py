from django.shortcuts import render , redirect
from .models import *
from django.db.models import Q
from foodapp.filters import RecipeFilter
from django_filters.rest_framework import DjangoFilterBackend
import json
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.views.generic import ListView
from django.contrib.postgres.search import SearchVector , SearchQuery, SearchRank
from django.http import StreamingHttpResponse



def index(request):
    search_queries = []
    tags = request.GET.get('tags') if request.GET.get('tags') != None else ''
    if tags:
        tags_list = json.loads(tags)
        search_queries = [item["value"] for item in tags_list]
        recipes = Recipe.objects.only('ingredient__ingredient_name__name')\
                        .prefetch_related('ingredient').\
                        filter(ingredient__ingredient_name__name__in=search_queries).distinct('id')
    else:
        recipes = Recipe.objects.all()


    context = {
        'recipes' : recipes
    }
    return render(request , 'index.html' , context)

 
# class index2(ListView):
#     template_name = 'index.html'

#     def get_queryset(self):
#         filterset = RecipeFilter(self.request.GET, queryset=Recipe.objects.all())
#         if filterset.is_valid():
#             return filterset.qs
#         else:
#             raise ValidationError(filterset.errors)

#     def handle_no_permission(self):
#         return JsonResponse(data={"error": "You do not have permission to access this view"}, status=403)



def stream_large_text_file(request):
    # An example of a large text file
    large_text_file_path = '/path/to/your/large/text/file.txt'

    def read_file(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                yield line

    response = StreamingHttpResponse(read_file('C:/Users/eng.Rabee/Django Projects/foodpro/foodapp/report.txt'), content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename="large_text_file.txt"'
    return response





def contact(request):
    if request.method =='POST':
        message = Messages.objects.get_or_create(
            writer=request.POST['name'],
            email = request.POST['email'],
            message=request.POST['message']
        )
        return redirect('contact')
    return render(request , 'contact.html')


# def blog(request):
#     blogs = Blog.objects.all()
#     context = {
#         'blogs' : blogs
#     }
#     return render(request,'blog.html' , context)



class ListBlogs(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    paginate_by = 3




def test(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ''
    recipes = Recipe.objects.filter(ingredient__ingredient_name__name__contains = q).distinct()

    context = {
        'recipes' : recipes
    }
    return render(request,'test.html' , context)


def single_blog(request, pk):
    blog = Blog.objects.get(id=pk)

    context = {
        'blog' : blog,

    }
    return render(request,'single-blog.html' , context)


def about(request):
    context = {
        
    }
    return render(request , 'about.html' , context)