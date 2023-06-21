from django.db import models
from apps.account.models import User

# Create your models here.

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimeStampModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=60, blank=True, null=True)
    post_description = models.CharField(max_length=250, blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class Like(TimeStampModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_by")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="blog_post")

    def __str__(self):
        return f'{self.user} {self.post.title}'