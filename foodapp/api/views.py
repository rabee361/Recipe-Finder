from rest_framework.decorators import api_view , APIView
from rest_framework.response import Response
from .serializers import *
from foodapp.filters import RecipeFilter
from foodapp.models import *
from django.contrib.postgres.search import SearchVector, SearchRank ,SearchQuery
from django.db.models import Q
import json
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView , RetrieveAPIView ,CreateAPIView

#### Basic ORM Filtering ######
class All_Recipes(APIView):
    def get(self,request):
        q = request.GET.get('tags')
        if q:
            q_list = json.loads(q)
            search_queries = [item["value"] for item in q_list]

        recipes = Recipe.objects.only('ingredient__ingredient_name__name')\
                                .prefetch_related('ingredient')\
                                .filter(ingredient__ingredient_name__name__icontains=search_queries).distinct('id')
  
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)

### Using Backend Filtering ###
class All_Recipes2(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilter


##### Using BackEnd filtering with the original #####
class All_Recipes3(APIView):
    def get(self,request):
        q = request.GET.get('tags')
        if q:
            q_list = json.loads(q)
            search_queries = [item["value"] for item in q_list]

        queryset = Recipe.objects.only('ingredient__ingredient_name__name')\
                                 .prefetch_related('ingredient')\
                                 .distinct('id')

        filterset = RecipeFilter(request.GET, queryset=queryset)
        if filterset.is_valid():
            print("hi")
            recipes = filterset.qs
        else:
            return Response(filterset.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)






class GetBlogs(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = PageNumberPagination
    throttle_classes = [AnonRateThrottle]


class GetSingleBlog(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CreateMessage(CreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer


class GalleryImages(ListAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GallerySerializer