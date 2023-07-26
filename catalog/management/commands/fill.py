from django.core.management import BaseCommand

from catalog.models import Product, Category
from datetime import date


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'name': 'Кроссовки'},
            {'name': 'Одежда'},
        ]

        for category_item in category_list:
            Category.objects.create(**category_item)

        category_sneakers = Category.objects.get(name='Кроссовки')
        category_clothes = Category.objects.get(name='Одежда')

        product_list = [
            {'name': 'Nike', 'category': category_sneakers, 'price': '12', 'date_make': date.today().isoformat(),
             'date_update':  date.today().isoformat()},
            {'name': 'Adidas', 'category': category_sneakers, 'price': '14', 'date_make': date.today().isoformat(),
             'date_update': date.today().isoformat()},
            {'name': 'Майка Nike', 'category': category_clothes, 'price': '20', 'date_make': date.today().isoformat(),
             'date_update': date.today().isoformat()},
            {'name': 'Футболка Adidas', 'category': category_clothes, 'price': '17', 'date_make': date.today().isoformat(),
             'date_update': date.today().isoformat()},
        ]

        for product_item in product_list:
            Product.objects.create(**product_item)
