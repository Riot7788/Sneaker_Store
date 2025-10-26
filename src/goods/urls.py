from django.urls import path


from .views import (
    catalog,
    product,
)


urlpatterns = [
    path('', catalog, name='index'),
    path('product/', product, name="product"),
]