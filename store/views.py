from django.http import request
from django.shortcuts import get_object_or_404, render
from .models import Category ,Product 
# Create your views here.

def all_products(request):
    product = Product.objects.all()
    return render(request  , 'store/home.html' , {'products' : product})
    print(product)

def categories(request):
    return {
        "categories": Category.objects.all(),
    }


def product_detail(request, slug):
    '''
    a revoir
    '''
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})
