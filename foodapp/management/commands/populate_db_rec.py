import random
from django.core.management.base import BaseCommand
from foodapp.models import *



class Command(BaseCommand):
    help = "Populates the database with random generated data."

    def add_arguments(self,parser):
        parser.add_argument("--amount", type=int, help="The number of purchases that should be created.")

    def handle(self, *args, **options):

        f = list()
        for i in range(0,2500):
            j = Ingredient.objects.get(id=(i+7))
            f.append(j)

        amount = options["amount"] if options["amount"] else 2500
        for i in range(0,amount):
            recipe = Recipe.objects.create(
                name=str(i)
            )
            for z in range(random.randint(1,10)):
                recipe.ingredient.add(random.choice(f))
            recipe.save()

        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))
