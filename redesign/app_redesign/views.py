from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponseNotFound
# Create your views here.

from .models import Product

def indexpage(request):
    products = Product.objects.all()
    return render(request, "index.html", {"articles": products, "page": "index"})

def postpage(request):
    return render(request, "post.html", {"page": "post"})

def aboutpage(request):
    return render(request, "about.html", {"page": "about"})



def contactpage(request):
    if request.method == "GET":
        return render(request, "contact.html", {"page": "contact"})
    else:
        print(request.POST)

def contactpage(request):
    if request.method == "GET":
        return render(request, "contact.html", {"page": "contact"})
    else:
        print(request.POST)
        return redirect(contactpage)

def productpage(request):
    products = Product.objects.all()
    #product_images = ProductImage.objects.all()  # Предположим, что у вас есть модель ProductImage для фото продуктов
    return render(request, "product.html", {"products": products})#, "product_images": product_images})

#def add_image(request, product_id):
#    if request.method == "POST":
#        product = Product.objects.filter(id=product_id).first()
#        if product and 'image' in request.FILES:
#            product_image = ProductImage()
#            product_image.product = product
#            product_image.image = request.FILES['image']
#            product_image.save()
#            return redirect('product_page')

#    return HttpResponseNotFound("404")