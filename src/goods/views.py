from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import (
    Categories,
    Products,
)
from .utils import q_search


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

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