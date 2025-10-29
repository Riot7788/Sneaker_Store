from django.shortcuts import render, get_object_or_404
from .models import (
    Categories,
    Products,
)


def catalog(request):
    categories = Categories.objects.all()
    products = Products.objects.all()
    return render(request, "goods/catalog.html", {"categories": categories, "products": products})


def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, "goods/product.html", {"product": product})