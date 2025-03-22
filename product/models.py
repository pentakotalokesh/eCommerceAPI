from django.db import models
import uuid


class Category(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100)
    
    class Meta:
        db_table='Category'
        
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,related_name="subcategories",on_delete=models.CASCADE)
    
    class Meta:
        db_table='SubCategory'
        
    def __str__(self):
        return self.name
    


class Product(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    SubCategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    desc=models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock_quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=(('active', 'Active'), ('inactive', 'Inactive')), default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='Product'
    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="images")
    image_url = models.URLField()
    
    class Meta:
        db_table='ProductImage'
    
    def __str__(self):
        return self.product.name