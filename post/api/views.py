from rest_framework import viewsets
from ..models import Post
from .serializers import PostSerializer
from .permissions import PostPermission
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [PostPermission]

    def get_queryset(self):
        try:
            if self.request.user.post.all():
                return self.request.user.post.all()

            if self.request.user.profile.isFamily:
                return Post.objects.filter(can_family_access=True)
            elif self.request.user.profile.isFriend:
                return Post.objects.filter(can_friend_access=True)
            elif self.request.user.profile.isSubscriber:
                return Post.objects.filter(can_subcriber_access=True)
            else:
                return Post.objects.filter(can_anonymous_user_access=True)
        except AttributeError:
            return Post.objects.filter(can_anonymous_user_access=True)
