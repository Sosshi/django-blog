from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name="post", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="blog_images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    can_family_access = models.BooleanField(default=True)
    can_friend_access = models.BooleanField(default=True)
    can_subcriber_access = models.BooleanField(default=True)
    can_anonymous_user_access = models.BooleanField(default=True)

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
