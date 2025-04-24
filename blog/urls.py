from django.urls import path
from .views import index, post_detail, create_post, update_post, delete_post, register, user_login, user_logout, contact, profile, settings, dashboard

urlpatterns = [
    path('',index, name = "homepage"),
    path('post/<int:pk>/', post_detail, name="post_detail"),
    path('create/', create_post, name = "create_post"),
    path('update/<int:pk>/', update_post, name = "update_post"),
    path('delete/<int:pk>/', delete_post, name = "delete_post"),
    path('register/', register, name = "register"),
    path('login/', user_login, name = "login"),
    path('logout/', user_logout, name = 'logout'),
    path('contact/', contact, name='contact'),
    path('profile/', profile, name='profile'),
    path('settings/', settings, name='settings'),
    path('dashboard/', dashboard, name='dashboard'),
]