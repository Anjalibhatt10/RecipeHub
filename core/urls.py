from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from home.views import home
from vege.views import (
    receipes,
    my_recipes,
    delete_recipe,
    edit_recipe,
    dashboard,
    like_recipe,
    recipe_detail,
)

urlpatterns = [

    # Open login page first
    path(
        '',
        RedirectView.as_view(
            url='/accounts/login/',
            permanent=False
        )
    ),

    # Authentication
    path(
        'accounts/',
        include('accounts.urls')
    ),

    # Home Page
    path(
        'home/',
        home,
        name='home'
    ),

    # Creator Pages
    path(
        'receipes/',
        receipes,
        name='receipes'
    ),

    path(
        'my-recipes/',
        my_recipes,
        name='my_recipes'
    ),

    path(
        'edit-recipe/<int:id>/',
        edit_recipe,
        name='edit_recipe'
    ),

    path(
        'delete-recipe/<int:id>/',
        delete_recipe,
        name='delete_recipe'
    ),

    path(
        'recipe/<int:id>/',
         recipe_detail,
         name='recipe_detail'
    ),

    # Like Recipe
    path(
        'like-recipe/<int:id>/',
        like_recipe,
        name='like_recipe'
    ),

    # Admin
    path(
        'admin/',
        admin.site.urls
    ),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )