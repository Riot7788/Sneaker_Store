from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name='Скидка в %')
    category = models.ForeignKey(
        to=Categories,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    SIZE_CHOICES = [
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
    ]

    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='sizes',
        verbose_name="Продукт"
    )
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, verbose_name="Размер")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")

    class Meta:
        db_table = "product_size"
        verbose_name = "Размер обуви"
        verbose_name_plural = "Размеры обуви"
        unique_together = ('product', 'size')

    def __str__(self):
        return f"{self.product.name} — размер {self.size} ({self.quantity} шт.)"
