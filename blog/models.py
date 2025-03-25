from django.db import models
from django.contrib.auth.models import User

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']