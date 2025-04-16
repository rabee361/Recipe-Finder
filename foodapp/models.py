from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Ingredient_name(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Ingredient(models.Model):
    ingredient_name = models.ForeignKey(Ingredient_name , on_delete=models.CASCADE , db_index=True)
    quantity = models.IntegerField()
    unit = models.ForeignKey(Unit , on_delete=models.CASCADE)

    def __str__(self):
        return str(self.quantity)+" "+str(self.unit)+" "+str(self.ingredient_name)


class Cuisine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Recipe(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='images/')
    ingredient = models.ManyToManyField(Ingredient)
    cuisine = models.ForeignKey(Cuisine , on_delete=models.CASCADE)
    time_to_cook = models.DurationField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    topic = models.CharField(max_length=50)
    text = models.TextField(max_length=1500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic


class Messages(models.Model):
    writer = models.CharField(max_length=50)
    email = models.EmailField(default=None)
    message = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message[0:50]


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
