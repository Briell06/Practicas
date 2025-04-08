from django.urls import path
from .views import (
    ItemList,
    ItemDetail,
    CompanyList,
    CompanyDetail,
    CommentList,
    CommentDetail,
)


urlpatterns = [
    # Items
    path("items/", ItemList.as_view(), name="item-list"),
    path("items/<int:pk>/", ItemDetail.as_view(), name="item-detail"),
    # Companies
    path("companies/", CompanyList.as_view(), name="company-list"),
    path("companies/<int:pk>/", CompanyDetail.as_view(), name="company-detail"),
    # Comments
    path("comments/", CommentList.as_view(), name="comment-list"),
    path("comments/<int:pk>/", CommentDetail.as_view(), name="comment-detail"),
]
