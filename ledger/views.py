from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage, Profile
from .forms import RecipeForm, RecipeImageForm

@login_required
def recipe(request, num=1):
    recipe = Recipe.objects.get(pk=num)
    recipes = Recipe.objects.all()
    ingredients = RecipeIngredient.objects.filter(recipe=recipe, ingredient__recipe__recipe__name=recipe.name)
    return render(request, 'recipe.html', {'recipe':recipe,
                                           'ingredients':ingredients,
                                           'recipes':recipes,})

@login_required
def recipe_list_context(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes_list.html', {'recipes':recipes})

@login_required
def recipe_add(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        image_form = RecipeImageForm(request.POST, request.FILES)

        if recipe_form.is_valid() and image_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = Profile.objects.get(user=request.user)
            recipe.save()

            recipe_image = image_form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()

            ingredient_ids = request.POST.getlist('ingredient')
            quantities = request.POST.getlist('quantity')

            for ingredient_id, quantity in zip(ingredient_ids, quantities):
                ingredient = Ingredient.objects.get(id=ingredient_id)
                RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient, quantity=quantity)

            return HttpResponseRedirect('/recipes/list')

    recipe_form = RecipeForm()
    image_form = RecipeImageForm()
    ingredients = Ingredient.objects.all()
    
    return render(request, 'recipe_add.html', {
        'form': recipe_form,
        'image_form': image_form,
        'ingredients': ingredients
    })

@login_required
def add_recipe_image(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()

            recipe.updated_on = timezone.now()
            recipe.save()
            
            return HttpResponseRedirect(f'/recipe/{pk}')

    form = RecipeImageForm()
    return render(request, 'add_recipe_image.html', {'form': form, 'recipe': recipe})
