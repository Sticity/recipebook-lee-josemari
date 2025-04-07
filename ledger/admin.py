from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Ingredient, Recipe, RecipeIngredient, RecipeImage

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    search_fields = ('name',)
    list_display = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    search_fields = ('name',)
    list_display = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    search_fields = ('recipe__name', 'ingredient__name',)
    list_display = ('recipe__name', 'ingredient__name', 'quantity', )
    list_filter = ('recipe__name', )

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage

    search_fields = ('recipe__name',)
    list_display = ('recipe__name',)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline,]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
