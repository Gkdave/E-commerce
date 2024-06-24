from django.shortcuts import render
from .models import Product 

def get_product(request,slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {'product':product}
        
        return render(request,'products/product.html',context=context)
    except Exception as e:
        print(e)