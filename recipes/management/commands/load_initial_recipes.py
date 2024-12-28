from django.core.management.base import BaseCommand
from recipes.models import Recipe

class Command(BaseCommand):
    help = 'Loads initial recipe data'

    def handle(self, *args, **kwargs):
        initial_recipes = [
            {
                "name": "Margherita Pizza",
                "ingredients": {"basil": 10, "flour": 500, "yeast": 1, "mozzarella": 200, "tomato_sauce": 150},
                "time_to_make": 30,
                "image_url": "https://cdn.loveandlemons.com/wp-content/uploads/opengraph/2023/07/margherita-pizza-recipe.jpg",
                "message": "The best pizza in the world!",
                "is_liked": False
            },
            # Add more recipes here...
        ]

        for recipe_data in initial_recipes:
            Recipe.objects.get_or_create(**recipe_data)

        self.stdout.write(self.style.SUCCESS('Successfully loaded initial recipes')) 