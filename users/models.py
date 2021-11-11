from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    All the extra fields needed are placed in the UserProfile model
    """

    pass


class UserProfile(models.Model):
    """
    This contains all the user profile
    it is related to the user Model
    """

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    about = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="profile_images")
    isFamily = models.BooleanField(default=False)
    isFriend = models.BooleanField(default=False)
    isSubscriber = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_image(self):
        if self.image:
            return self.image.url

        else:
            return ""

    def __str__(self):
        return str(self.user)
