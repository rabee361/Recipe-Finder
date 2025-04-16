from .models import Recipe
import django_filters


class RecipeFilter(django_filters.FilterSet):
    ingredients = django_filters.CharFilter(field_name='ingredient__ingredient_name__name', lookup_expr='icontains')

    class Meta:
        model = Recipe
        fields = ['ingredients']