from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

class Comment(models.Model):
    username = models.CharField(max_length=25)
    content = models.TextField()
    created_at = models.DateTimeField()
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)


