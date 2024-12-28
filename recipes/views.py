from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from flask import jsonify
from .models import Recipe
from django.core.serializers.json import DjangoJSONEncoder
import json




def tester(request, start: int = 2, end: int = 20):
    return render(request, "data.html", {"data": list(Recipe.objects.filter(id__range = (start, end), is_liked = False).values())})
def home(request):
    users = [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "password123"
        },
        {
            "id": 2,
            "name": "Jane Doe",
            "email": "jane.doe@example.com",
            "password": "password123"
        },
        {
            "id": 3,
            "name": "John Smith",
            "email": "john.smith@example.com",
            "password": "password123"
        },
        {
            "id": 4,
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "password": "password123"
        },
        {
            "id": 5,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "password123"
        },
    ]
    
    context = {
        'users_json': json.dumps(users),
    }
    return render(request, 'index.html', context)

def all_recipies(request):
    recipes = Recipe.objects.all()
    recipe_data = []
    
    for recipe in recipes:
        recipe_data.append({
            "id": recipe.id,
            "name": recipe.name,
            "ingredients": recipe.ingredients,
            "time_to_make": recipe.time_to_make,
            "image_url": recipe.image_url,
            "message": recipe.message,
            "is_liked": recipe.is_liked
        })
    
    return JsonResponse({"recipies": recipe_data})