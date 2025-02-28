from django.urls import path
from .views import recipe, recipe_list_context

urlpatterns = [
    path('recipe/<int:num>/', recipe, name="recipe"),
    path('recipes/list/', recipe_list_context, name="recipe_list_context"),
]

app_name = "ledger"
