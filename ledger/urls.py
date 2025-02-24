from django.urls import path
from .views import recipe1

urlpatterns = [
    path('recipe/1/', recipe1, name="recipe1"),
]

app_name = "ledger"
