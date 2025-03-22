from rest_framework import serializers
from .models import Category,SubCategory,Product,ProductImage


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["id","name"]
        
class subCategorySerializer(serializers.ModelSerializer):
    category = categorySerializer(read_only=True)
    class Meta:
        model=SubCategory
        fields=["id","name","category"]
        
        
#Product Serializers

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields='__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    category = categorySerializer(read_only=True)
    images = ProductImageSerializer( many=True,read_only=True)
    class Meta:
        model=Product
        fields='__all__'
        


        