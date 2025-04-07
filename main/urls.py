from django.urls import path
from .views import index, item_detail, create_item


urlpatterns = [
    path("", index, name="home"),
    path("<int:pk>/", item_detail, name="item-detail"),
    path("create/", create_item, name="create-item"),
]
