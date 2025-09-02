# menu/views.py
from rest_framework import generics, permissions
from .models import Category, MenuItem
from .serializers import  CategorySerializers, MenuItemSerializers


# --------------------------
# Category Views
# --------------------------
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [permissions.AllowAny]  # Anyone can view/add categories


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [permissions.AllowAny]


# --------------------------
# MenuItem Views
# --------------------------
class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializers
    permission_classes = [permissions.AllowAny]


class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializers
    permission_classes = [permissions.AllowAny]
