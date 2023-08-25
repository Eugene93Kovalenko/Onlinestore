from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to="category/%Y/%m/%d/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_name": self.name.lower()})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"


class Product(models.Model):
    class ColorChoices(models.TextChoices):
        Black = "Black"
        Red = "Red"
        White = "White"
        Yellow = "Yellow"
        Blue = "Blue"
        Green = "Green"

    COLLECTION_CHOICE = [
        ("winter", "Winter"),
        ("spring", "Spring"),
        ("summer", "Summer"),
        ("autumn", "Autumn"),
    ]

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="products")
    # color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="products")
    color_choices = models.CharField(
        max_length=10, choices=ColorChoices.choices, blank=True
    )
    description = models.TextField(blank=False)
    information = models.TextField(blank=False)
    slug = models.SlugField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    num_visits = models.IntegerField(default=0)
    collection = models.CharField(max_length=10, choices=COLLECTION_CHOICE, blank=True)
    barcode_number = models.IntegerField(blank=False)
    category = models.ManyToManyField(Category, related_name="products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    def get_collection_absolute_url(self):
        return reverse("collection", kwargs={"collection_name": self.collection})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]


class ProductSizeColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='size')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='color')
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Товар - Размер - Цвет"
        verbose_name_plural = "Товар - Размер - Цвет"

    def __str__(self):
        return f"{self.product} - {self.size} - {self.color}"


class ProductImage(models.Model):
    image = models.ImageField(upload_to="product/%Y/%m/%d/")
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"

    def __str__(self):
        return self.image.name

    def get_absolute_url(self):
        return self.image.url
