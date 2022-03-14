from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.CharField(max_length=250)
    body_text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f"/posts/{self.pk}/"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.comment_text

