from django.shortcuts import render
from .models import Product 

def get_product(request,slug):
    product = Product.objects.get(slug=slug)
    context = {'products':product}
    
    return render(request,'products/product.html',{"products":product})