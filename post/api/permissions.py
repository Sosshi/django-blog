from rest_framework import permissions


class PostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            if obj.can_family_access and request.user.profile.isFamily:
                return True

            if obj.can_friend_access and request.user.profile.isFriend:
                return True

            if obj.can_subcriber_access and request.user.profile.isSubscriber:
                return True

        return False