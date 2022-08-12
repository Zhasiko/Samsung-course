from django.shortcuts import render
from .models import Product, VolumeType, Comment

# Create your views here.
def index(request):
    products = Product.objects.all()[:10]
    return render(request,'main/index.html',{"products" : products})

def authorize(request):
    return render(request, 'main/auth.html',{})

def about(request):
    return render(request, 'main/about.html',{})