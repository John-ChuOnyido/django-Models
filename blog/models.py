from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.

class Post(models.Model):

    # DB Fields
    Title = models.CharField(max_length=200)
    Text = models.TextField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="blog_posts"
    )
    
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

