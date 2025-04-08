from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ItemVS,
    CompanyVS,
    CommentVS,
    CommentCreate,
    CommentList,
)

router = DefaultRouter()
router.register("companies", CompanyVS, basename="companies")
router.register("items", ItemVS, basename="items")
router.register("comments", CommentVS, basename="comments")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "items/<int:pk>/comments/create/",
        CommentCreate.as_view(),
        name="comment-create",
    ),
    path("items/<int:pk>/comments/", CommentList.as_view(), name="comment-list"),
]
