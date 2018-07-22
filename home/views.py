from django.shortcuts import render
from product.models import *


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_jacet = products_images.filter(product__category__id=1)
    return render(request, 'home/home.html', locals())





# def home(request):
#     products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
#     products_images_laptops = products_images.filter(product__category_id=1)
#     products_images_phones = products_images.filter(product__category_id=2)
#     return render(request, 'landing/home.html', locals())
#     # locals return varrible
