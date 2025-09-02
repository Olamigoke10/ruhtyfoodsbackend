# menu/urls.py
from django.urls import path

from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    MenuItemListCreateView,
    MenuItemDetailView,
)

urlpatterns = [
    # Categories
    path("categories/", CategoryListCreateView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),

    # Menu Items
    path("items/", MenuItemListCreateView.as_view(), name="menuitem-list"),
    path("items/<int:pk>/", MenuItemDetailView.as_view(), name="menuitem-detail"),
]
