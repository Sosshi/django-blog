from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    friend = "Friend"
    subscriber = "Subscriber"
    family = "Family"

    RELATION = (("friend", friend), ("subscriber", subscriber), ("family", family))

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    about = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="profile_images")
    status = models.CharField(max_length=20, choices=RELATION)

    def get_image(self):
        if self.image:
            return self.image.url

        else:
            return ""

    def __str__(self):
        return str(self.user)
