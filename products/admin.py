from django.contrib import admin
from .models import Product, Category, Genre, Promotion


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_options',
    )


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class PromotionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product',
        'valid_from',
        'valid_to',
        'discount',
        'active',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Promotion, PromotionAdmin)
