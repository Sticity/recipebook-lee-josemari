from django.urls import path
from .views import recipe, recipe_list_context, recipe_add, add_recipe_image

urlpatterns = [
    path('recipe/<int:num>/', recipe, name='recipe'),
    path('recipes/list/', recipe_list_context, name='recipe_list_context'),
    path('recipe/add/', recipe_add, name='recipe_add'),
    path('recipe/<int:pk>/add_image/', add_recipe_image, name='add_recipe_image'),
]

app_name = 'ledger'
