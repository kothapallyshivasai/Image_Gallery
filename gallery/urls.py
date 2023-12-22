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
    path('profile/', profile, name="profile"),
    path('save_profile/', save_profile, name="save_profile"),
    path('delete_image/<int:id>', delete_image, name="delete_image"),
    path('update_image/<int:id>', update_image, name="update_image"),
    path('image_like/<int:image_id>', image_like, name="image_like"),
    path('remove_like/<int:image_id>', remove_like, name="remove_like"),
    path('add_comment/<int:image_id>', add_comment, name="add_comment"),
    path('remove_comment_profile/<int:comment_id>', remove_comment_profile, name="remove_comment_profile"),
    path('remove_like_profile/<int:like_id>', remove_like_profile, name="remove_like_profile"),
    path("liked_images/", liked_images, name="liked_images"),
    path("private_images/", private_images, name="private_images"),
    path("detailed_image/<int:id>", detailed_image, name="detailed_image"),
    path('download_image/<int:id>/', download_image, name='download_image'),
]
 