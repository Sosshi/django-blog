from rest_framework import serializers
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "title",
            "body",
            "image",
            "get_image",
            "created_at",
            "updated_at",
            "can_family_access",
            "can_friend_access",
            "can_subcriber_access",
            "can_anonymous_user_access",
        ]
