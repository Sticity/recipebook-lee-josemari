from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Ingredient, Recipe, RecipeIngredient

# Create your views here.
@login_required
def recipe(request, num=1):
    recipe = Recipe.objects.get(pk=num)
    recipes = Recipe.objects.all()
    ingredients = RecipeIngredient.objects.filter(recipe=recipe, ingredient__recipe__recipe__name=recipe.name)
    return render(request, 'recipe.html', {'recipe':recipe, 'ingredients':ingredients, 'recipes':recipes})

@login_required
def recipe_list_context(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes_list.html', {'recipes':recipes})
