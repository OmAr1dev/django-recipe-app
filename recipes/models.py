from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    """
    Model representing a recipe created by a user.

    Attributes:
        title (str): The title of the recipe.
        description (str): Optional short description of the recipe.
        ingredients (str): Ingredients listed, one per line.
        steps (str): Cooking steps listed, one per line.
        category (str): Optional category, e.g., Dessert, Main Course.
        cooking_time (int): Optional time in minutes required to cook.
        author (User): The user who created the recipe.
        created_at (datetime): Timestamp when recipe was created.
        updated_at (datetime): Timestamp when recipe was last updated.
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.TextField(help_text="One ingredient per line")
    steps = models.TextField(help_text="One step per line")
    category = models.CharField(max_length=100, blank=True)
    cooking_time = models.PositiveIntegerField(
        null=True, blank=True, help_text="Minutes"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the Recipe instance.
        """
        return self.title
