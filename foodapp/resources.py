from .models import *  
from import_export import resources

class IngredientsRes(resources.ModelResource):
    class Meta:
        model = Ingredient_name
        fields = ('id','name')