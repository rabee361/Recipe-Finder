from rest_framework import serializers
from foodapp.models import *


class RecipeSerializer(serializers.ModelSerializer):
    ingredient = serializers.StringRelatedField(read_only=True,many=True)
    class Meta:
        model = Recipe
        fields = ('name','ingredient')


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'