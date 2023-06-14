from django.db import models
from django.contrib.auth.models import User
# from django.utils.timezone import now



class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=130, unique=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
