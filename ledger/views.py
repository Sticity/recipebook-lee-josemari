from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Ingredient, Recipe, RecipeIngredient

# Create your views here.
def recipe1(request):
    rcp = Recipe.objects.get(pk=1)
    ingredients = RecipeIngredient.objects.filter(recipe=rcp, ingredient__recipe__recipe__name=rcp.name)
    return render(request, 'recipe.html', {'recipe':rcp, 'ingredients':ingredients})

def recipe2(request):
    rcp = Recipe.objects.get(pk=2)
    ingredients = RecipeIngredient.objects.filter(recipe=rcp, ingredient__recipe__recipe__name=rcp.name)
    return render(request, 'recipe.html', {'recipe':rcp, 'ingredients':ingredients})

def recipe_list_context(request):
    rcps = Recipe.objects.all()
    return render(request, 'recipes_list.html', {'recipes':rcps})
