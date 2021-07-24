from django.shortcuts import render
from .models import Category ,Product 
# Create your views here.

def all_products(request):
    product = Product.objects.all()
    return render(request  , 'store/home.html' , {'products' : product})
    