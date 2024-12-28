from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=200, default="New Recipe")
    ingredients = models.JSONField(default=dict)  # Empty dict as default
    time_to_make = models.IntegerField(default=30)  # 30 minutes default
    image_url = models.URLField(
        max_length=500, 
        default="https://via.placeholder.com/300x200?text=No+Image"
    )
    message = models.TextField(default="A delicious recipe!")
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        return f"Recipe(name={self.name}, ingredients={self.ingredients}, time_to_make={self.time_to_make}, image_url={self.image_url}, message={self.message}, is_liked={self.is_liked})"


    def __repr__(self):
        return self.name



# Recipe(name="Pizza", instructions="Bake the pizza in the oven").save()
# Recipe(name="steak", instructions="Cook the steak in the oven").save()
# Recipe(name="salad", instructions="Mix the salad in the oven").save()
# Recipe(name="soup", instructions="Cook the soup in the oven").save()
# Recipe(name="pasta", instructions="Cook the pasta in the oven").save()
# Recipe(name="rice", instructions="Cook the rice in the oven").save()
# Recipe(name="chicken", instructions="Cook the chicken in the oven").save()
# Recipe(name="fish", instructions="Cook the fish in the oven").save()
# Recipe(name="vegetable", instructions="Cook the vegetable in the oven").save()
