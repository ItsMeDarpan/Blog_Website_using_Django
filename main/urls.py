from django.urls import path
from .views import blog_list, blog_detail, create_post

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('post/<int:pk>/', blog_detail, name='blog_detail'),
    path('create/', create_post, name ='create_post'),
    
]