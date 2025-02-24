from django.urls import path
from .views import recipe1, recipe2, recipe_list_context

urlpatterns = [
    path('recipe/1/', recipe1, name="recipe1"),
    path('recipe/2/', recipe2, name="recipe2"),
    path('recipes/list/', recipe_list_context, name="recipe_list_context"),
]

app_name = "ledger"
