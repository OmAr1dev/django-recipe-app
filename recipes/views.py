from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Recipe


class RecipeForm(forms.ModelForm):
    """
    Form for creating a new Recipe instance.
    """

    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "steps",
            "category",
            "cooking_time",
        ]


def recipe_list(request):
    """
    View to display all recipes in the database.
    """
    recipes = Recipe.objects.all().order_by("-created_at")
    return render(request, "recipes/recipe_list.html", {"recipes": recipes})


@login_required
def recipe_detail(request, pk):
    """
    View to display details of a single recipe by primary key.
    """
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe})


@login_required
def recipe_create(request):
    """
    View to create a new recipe using a form.
    """
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # assuming logged-in user
            recipe.save()
            return redirect("recipes:detail", pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, "recipes/recipe_form.html", {"form": form})
