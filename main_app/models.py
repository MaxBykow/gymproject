from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ImageSQL(models.Model):
    picture = models.FileField(upload_to='base_images')
    title = models.TextField(default='', null=False)


class CommentModel(models.Model):
    data = models.DateTimeField(auto_now_add=True, null=False)
    text = models.TextField(default='', null=False, max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
