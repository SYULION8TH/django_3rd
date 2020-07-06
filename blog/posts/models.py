from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length= 100)
    body = models.TextField()
    img = models.ImageField(upload_to = "posts/image", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)