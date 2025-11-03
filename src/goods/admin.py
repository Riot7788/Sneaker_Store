from django.contrib import admin

from .models import (
    Categories,
    Products,
    ProductSize,
)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    search_fields = ('name',)


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1
    min_num = 1
    fields = ('size', 'quantity')
    verbose_name = "Размер"
    verbose_name_plural = "Размеры"


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'category', 'price', 'discount', 'final_price')
    list_filter = ('category', 'gender')
    search_fields = ('name', 'description')
    inlines = [ProductSizeInline]

    @admin.display(description='Цена со скидкой')
    def final_price(self, obj):
        return obj.sell_price()