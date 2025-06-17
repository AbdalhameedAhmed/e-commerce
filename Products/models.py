from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    image=models.ImageField(upload_to="photos/%y")

    def __str__(self):
        return self.name