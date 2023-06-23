from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=130, unique=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)


    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.user.username + " Comment: " + self.body