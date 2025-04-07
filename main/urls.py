from django.urls import path
from .views import ItemList, ItemDetail, CompanyList, CompanyDetail


urlpatterns = [
    path("items/", ItemList.as_view(), name="items"),
    path("items/<int:pk>/", ItemDetail.as_view(), name="item-detail"),
    path("companies/", CompanyList.as_view(), name="companies"),
    path("companies/<int:pk>/", CompanyDetail.as_view(), name="company-detail"),
]
