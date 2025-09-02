from django.db import models

# Create your models here.
class Category(models.Model): 
    name = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name
        

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu/')
    
    def __str__(self):
        return f"{self.name}  {self.price}"