from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    image=models.ImageField(upload_to="photos/%y")
    categories=models.ManyToManyField(Category,related_name="products")

    def __str__(self):
        return self.name
