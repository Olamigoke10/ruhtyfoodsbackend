from rest_framework import serializers
from .models import Category, MenuItem


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class MenuItemSerializers(serializers.ModelSerializer):
    
    category = CategorySerializers(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source = "category",
        write_only = True,
    )
    
    class Meta:
        model = MenuItem
        fields = [ "id",
                  "name", 
                  "price", 
                  "description", 
                  "image",
                  "category",
                  "category_id"
                  ]
