from django.shortcuts import render
from django.http import HttpResponse
from vege.models import Receipe


def home(request):

    queryset = Receipe.objects.all()

    # Search
    search = request.GET.get("search")

    if search:
        queryset = queryset.filter(
            name__icontains=search
        )

    # Category Filter
    category = request.GET.get("category")

    if category:
        queryset = queryset.filter(
            category=category
        )

    return render(
        request,
        "all_recipes.html",
        {
            "receipes": queryset
        }
    )


def success_page(request):
    return HttpResponse("<h1>Hey this is a Success Page</h1>")

