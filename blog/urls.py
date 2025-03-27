from django.urls import path
from .views import index, post_detail, create_post, update_post, delete_post, register

urlpatterns = [
    path('',index, name = "homepage"),
    path('post/<int:pk>/', post_detail, name="post_detail"),
    path('create/', create_post, name = "create_post"),
    path('update/<int:pk>/', update_post, name = "update_post"),
    path('delete/<int:pk>/', delete_post, name = "delete_post"),
    path('register/', register, name = "register"),
]