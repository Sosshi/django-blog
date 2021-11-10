from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from users.api.views import UserViewSet, UserProfileViewSet
from post.api.views import PostViewSet

router = routers.DefaultRouter()
router.register(r"profiles", UserProfileViewSet)
router.register(r"posts", PostViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include(router.urls)),
    path(r"auth/", include("djoser.urls")),
]
