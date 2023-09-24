from django.urls import path
from .views import *
from django.contrib.auth import views


urlpatterns = [
    path('home/', home_page, name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('user_home/', user_home, name="user_home"),
    path('upload_image/', upload_image, name="upload_image"),
    path('validate_upload_image/', validate_upload_image, name="validate_upload_image"),
    path('profile/', profile, name="profile")
]
