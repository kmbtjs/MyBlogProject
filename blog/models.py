from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name= models.CharField(max_length=50)
    comment = models.TextField(max_length=400)
    comment_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['comment_date']

    def __str__(self):
        return f'{self.post.title} {self.name}'

