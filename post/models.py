from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name="user", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="blog_images")

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def __str__(self):
        return self.title
