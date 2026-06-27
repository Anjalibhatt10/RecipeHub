from django.db import models
from django.contrib.auth.models import User


class Receipe(models.Model):

    CATEGORY_CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Dessert', 'Dessert'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(
        upload_to='receipes/',
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Lunch'
    )

    def __str__(self):
        return self.name


class Like(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    recipe = models.ForeignKey(
        Receipe,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user', 'recipe')     
    
