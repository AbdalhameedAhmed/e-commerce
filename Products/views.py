from django.shortcuts import render
from .models import Product
# Create your views here.

def products (request):
    product_list = Product.objects.all()
    return render(request,"products/index.html",context={"products":product_list})