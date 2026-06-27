from django.urls import path
from .views import register, login_page, logout_page

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]