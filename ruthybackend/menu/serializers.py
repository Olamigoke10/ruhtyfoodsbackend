from rest_framework import serializers
from .models import Category, MenuItem


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class MenuItemSerializers(serializers.ModelSerializers):
    
    category = CategorySerializers(read_only=True)
    category_id = serializers.PrimarykeyRelatedField(
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
