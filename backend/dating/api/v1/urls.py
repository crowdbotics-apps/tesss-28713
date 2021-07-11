from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    InboxViewSet,
    SettingViewSet,
    DislikeViewSet,
    LikeViewSet,
    UserPhotoViewSet,
    MatchViewSet,
    ProfileViewSet,
)

router = DefaultRouter()
router.register("userphoto", UserPhotoViewSet)
router.register("profile", ProfileViewSet)
router.register("setting", SettingViewSet)
router.register("like", LikeViewSet)
router.register("dislike", DislikeViewSet)
router.register("inbox", InboxViewSet)
router.register("match", MatchViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
