from rest_framework import serializers
from .models import Category, MenuItem


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class MenuItemSerializers(serializers.ModelSerializers):
    class Meta:
        model = MenuItem
        fields = 

