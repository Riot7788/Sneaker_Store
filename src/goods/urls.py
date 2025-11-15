from django.urls import path


from .views import (
    catalog,
    product,
    product_detail,
)


urlpatterns = [
    path('search/', catalog, name='search'),
    path('', catalog, {'category_slug': 'all'}, name='catalog_all'),
    path('<slug:category_slug>/', catalog, name='index'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('product/<slug:product_slug>/', product, name="product"),
]