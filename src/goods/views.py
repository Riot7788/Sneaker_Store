from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import (
    Categories,
    Products,
)


def catalog(request, category_slug, page=1):
    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    categories = Categories.objects.all()

    paginator = Paginator(goods, 6)
    page_obj = paginator.page(page)

    context = {
        "categories": categories,
        "goods": page_obj,
        "slug_url": category_slug,
    }

    return render(
        request=request,
        template_name="goods/catalog.html",
        context=context
    )


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product,
    }

    return render(
        request=request,
        template_name="goods/product.html",
        context=context
    )

def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, "goods/product.html", {"product": product})