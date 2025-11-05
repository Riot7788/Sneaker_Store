from django.urls import path


from .views import (
    catalog,
    product,
    product_detail,
)


urlpatterns = [
    path('', catalog, {'category_slug': 'all'}, name='catalog_all'),
    path('<slug:category_slug>/', catalog, name='index'),
    path('<slug:category_slug>/<int:page>/', catalog, name='index'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
]