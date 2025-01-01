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



# recipes_data = [
#     {"name": "Pizza", "message": "Bake the pizza in the oven"},
#     {"name": "Steak", "message": "Cook the steak in the oven"},
#     {"name": "Salad", "message": "Mix the salad in the oven"},
#     {"name": "Soup", "message": "Cook the soup in the oven"},
#     {"name": "Pasta", "message": "Cook the pasta in the oven"},
#     {"name": "Rice", "message": "Cook the rice in the oven"},
#     {"name": "Chicken", "message": "Cook the chicken in the oven"},
#     {"name": "Fish", "message": "Cook the fish in the oven"},
#     {"name": "Vegetable", "message": "Cook the vegetable in the oven"},
# ]

# for recipe in recipes_data:
#     Recipe(**recipe).save()

