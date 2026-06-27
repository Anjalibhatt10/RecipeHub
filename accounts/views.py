from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile


def register(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        # Password check
        if password != confirm_password:
            return render(request, "register.html", {
                "error": "Passwords do not match."
            })

        # Username exists
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists."
            })

        # Email exists
        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {
                "error": "Email already registered."
            })

        # Create User
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create Profile
        Profile.objects.create(
            user=user,
            role=role
        )

        return redirect('/accounts/login/')

    return render(request, "register.html")




def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:

            return render(
                request,
                "login.html",
                {
                    "error": "❌ Invalid username or password."
                }
            )

        login(request, user)

        print("Logged in:", user.username)
        print("Role:", user.profile.role)

        return redirect("/home/")

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect('/accounts/login/')