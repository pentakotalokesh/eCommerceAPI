from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category,SubCategory,Product

from .serializers import categorySerializer,subCategorySerializer,ProductSerializer
from .permissions import IsAdminOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    
    """
    A Simple ViewSet to list Categories
    """
    queryset = Category.objects.all()
    serializer_class = categorySerializer
    lookup_field="name"
    permission_classes=[IsAdminOrReadOnly]
    
"""     def retrieve(self,request,pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data) """
    
    
class SubCategoryViewSet(viewsets.ModelViewSet):
    
    """
    A Simple ViewSet to Subcategories
    """
    queryset=SubCategory.objects.all()
    serializer_class=subCategorySerializer
    permission_classes=[IsAdminOrReadOnly]
    
    
    
#Product ViewSets
class ProductViewSet(viewsets.ModelViewSet):
    """
    A Simple ViewSet to CRUD for Product
    """
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="name"
    permission_classes=[IsAdminOrReadOnly]
        