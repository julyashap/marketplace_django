import json

from django.core.management import BaseCommand
from catalog.models import Product, Category
import os.path


class Command(BaseCommand):
    """Команда для наполнения БД данными с JSON-файла"""

    @staticmethod
    def json_read_categories():
        """Метод для получения данных о категориях с JSON-файла"""

        with open('catalog.json', encoding='utf-8') as jsonfile:
            content = json.load(jsonfile)

        categories = []
        for note in content:
            if note['model'] == 'catalog.category':
                categories.append({'pk': note['pk'], 'fields': note['fields']})

        return categories

    @staticmethod
    def json_read_products():
        """Метод для получения данных о продуктах с JSON-файла"""

        with open('catalog.json', encoding='utf-8') as jsonfile:
            content = json.load(jsonfile)

        products = []
        for note in content:
            if note['model'] == 'catalog.product':
                products.append({'pk': note['pk'], 'fields': note['fields']})

        return products

    def handle(self, *args, **options):
        """Метод, который реализует логику наполнения БД данными с JSON-файла"""

        # удаление всех объектов Category и Product
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category['pk'], name=category['fields']['name'],
                         description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(pk=product['pk'], name=product['fields']['name'], description=product['fields']['description'],
                        preview=product['fields']['preview'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'], created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'])
            )

        Product.objects.bulk_create(product_for_create)
