from django.core.cache import cache
from catalog.models import Category, Product
from config.settings import ENABLE_CACHE


def cache_category_list():
    if ENABLE_CACHE:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list


def cache_product_list(category_pk):
    if ENABLE_CACHE:
        key = f'product_list_{category_pk}'
        product_list = cache.get(key)
        if product_list is None:
            category = Category.objects.get(pk=category_pk)
            product_list = Product.objects.filter(category=category)
            cache.set(key, product_list)
    else:
        category = Category.objects.get(pk=category_pk)
        product_list = Product.objects.filter(category=category)
    return product_list
