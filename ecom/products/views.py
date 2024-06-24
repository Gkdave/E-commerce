from django.shortcuts import render
from .models import Product 

def get_product(request,slug):
    
    product = Product.objects.get(slug=slug)
    context = {'product':product}
    if request.GET.get('size'):
        size = request.GET.get('size')
        #print(size)
        price = product.get_product_price_by_size(size)
        context['selected_size'] = size
        context['updated_price'] = price 
        print(price)
    return render(request,'products/product.html',context=context)
