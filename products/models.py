from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.admin.actions import delete_selected


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    GAMES = 'Games'
    CONSOLES = 'Consoles'
    ACCESSORIES = 'Accessories'
    ALL_PRODUCTS = 'All Products'
    Category_Range = (
        (GAMES, 'Games'),
        (CONSOLES, 'Consoles'),
        (ACCESSORIES, 'Accessories'),
        (ALL_PRODUCTS, 'All Products'),
    )

    category_options = models.CharField(max_length=16, choices=Category_Range, null=True, blank=True)


class Genre(models.Model):

    class Meta:
        verbose_name_plural = 'Genre'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(1),
                                               MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.name
