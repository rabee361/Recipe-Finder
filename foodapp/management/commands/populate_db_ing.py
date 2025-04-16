import random
from foodapp.models import *
from django.core.management.base import BaseCommand





class Command(BaseCommand):
    help = "Populates the database with random generated data."
    def add_arguments(self,parser):
        parser.add_argument("--amount", type=int, help="The number of ingredients that should be created.")

    def handle(self, *args, **options):
        ingredients_name = Ingredient_name.objects.all().values("name")
        x = list()
        for ingredient in ingredients_name:
            x.append(ingredient['name'])
        
        units = Unit.objects.all().values("name")
        y = list()
        for unit in units:
            y.append(unit['name'])

        z = ['1','2','3','4','5','100','200','300','400','500']

        amount = options["amount"] if options["amount"] else 2500

        for i in range(0,amount):
            j = Ingredient_name.objects.get(name=random.choice(x))
            n = Quantity.objects.get(name=random.choice(z))
            m = Unit.objects.get(name=random.choice(y))
            ingredient = Ingredient.objects.create(
                ingredient_name=j,
                quantity=n,
                unit=m
            )
            ingredient.save()

        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))