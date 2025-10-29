from django.urls import path


from .views import (
    catalog,
    product_detail,
)


urlpatterns = [
    path('', catalog, name='index'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
]