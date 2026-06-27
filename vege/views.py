from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Receipe
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Like

from accounts.models import Profile
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required




@login_required(login_url='/accounts/login/')
def receipes(request):

    profile, created = Profile.objects.get_or_create(
    user=request.user,
    defaults={"role": "Viewer"}
)

    if profile.role != "Creator":
        return HttpResponse("""
        <h1 style='text-align:center;margin-top:80px;'>
        🚫 Access Denied
        <br><br>
        Only Creators can add recipes.
        </h1>
        """)

    if request.method == "POST":

        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        category = data.get('category')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(
            user=request.user,
            name=receipe_name,
            description=receipe_description,
            image=receipe_image,
            category=category
        )

    queryset = Receipe.objects.filter(user=request.user)

    return render(
        request,
        'receipes.html',
        {'receipes': queryset}
    )


@login_required(login_url='/accounts/login/')
def my_recipes(request):

    receipes = Receipe.objects.filter(
        user=request.user
    )

    return render(
        request,
        'my_recipes.html',
        {'receipes': receipes}
    )



@login_required(login_url='/accounts/login/')
def delete_recipe(request, id):

    recipe = get_object_or_404(
        Receipe,
        id=id,
        user=request.user
    )

    recipe.delete()

    return redirect('/my-recipes/')



@login_required(login_url='/accounts/login/')
def edit_recipe(request, id):

    recipe = get_object_or_404(
        Receipe,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        recipe.name = request.POST.get('receipe_name')
        recipe.description = request.POST.get('receipe_description')

        if request.FILES.get('receipe_image'):
            recipe.image = request.FILES.get('receipe_image')

        recipe.save()

        return redirect('/my-recipes/')

    return render(
        request,
        'edit_recipe.html',
        {'recipe': recipe}
    )


@login_required(login_url='/accounts/login/')
def dashboard(request):

    total_recipes = Receipe.objects.filter(
        user=request.user
    ).count()

    context = {
        'total_recipes': total_recipes
    }

    return render(
        request,
        'dashboard.html',
        context
    )
@login_required(login_url='/accounts/login/')
def all_recipes(request):

    queryset = Receipe.objects.all()

    search = request.GET.get('search')

    if search:
        queryset = queryset.filter(
            name__icontains=search
        )

    return render(
        request,
        'all_recipes.html',
        {'receipes': queryset}
    )



@login_required(login_url='/accounts/login/')
def like_recipe(request, id):

    recipe = Receipe.objects.get(id=id)

    Like.objects.get_or_create(
        user=request.user,
        recipe=recipe
    )

    return redirect('/home/')

@login_required(login_url='/accounts/login/')
def recipe_detail(request, id):
    recipe = get_object_or_404(Receipe, id=id)

    return render(
        request,
        "recipe_detail.html",
        {"recipe": recipe}
    )