import json

from django.core.management import BaseCommand
from catalog.models import Product, Category
import os.path


class Command(BaseCommand):
    """Команда для наполнения БД данными с JSON-файла"""

    @staticmethod
    def json_read_categories():
        """Метод для получения данных о категориях с JSON-файла"""

        with open(os.path.join('..', '..', '..', 'catalog.json')) as jsonfile:
            content = json.loads(jsonfile)

        categories = [note for note in content if note['model'] == 'catalog.category']

        return categories

    @staticmethod
    def json_read_products():
        """Метод для получения данных о продуктах с JSON-файла"""

        with open(os.path.join('..', '..', '..', 'catalog.json')) as jsonfile:
            content = json.loads(jsonfile)

        products = [note for note in content if note['model'] == 'catalog.product']

        return products

    def handle(self, *args, **options):
        """Метод, который реализует логику наполнения БД данными с JSON-файла"""

        # удаление всех объектов Category и Product
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['name'], description=category['description'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['name'], description=product['description'], preview=product['preview'],
                        category=Category.objects.get(pk=product['category_id']), price=product['price'],
                        created_at=product['created_at'], updated_at=product['updated_at'])
            )

        Product.objects.bulk_create(product_for_create)
