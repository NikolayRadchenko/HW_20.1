from django.core.management import BaseCommand

from catalog.models import Sneakers, Blouses, Pants, Socks, Category
from datetime import date


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Sneakers.objects.all().delete()

        category_list = [
            {'name': 'Кроссовки'},
            {'name': 'Кофты'},
            {'name': 'Штаны'},
            {'name': 'Носки'},
        ]

        for category_item in category_list:
            Category.objects.create(**category_item)

        category_sneakers = Category.objects.get(name='Кроссовки')
        category_blouses = Category.objects.get(name='Кофты')
        category_pants = Category.objects.get(name='Штаны')
        category_socks = Category.objects.get(name='Носки')

        product_list = [
            {'name': 'Nike', 'category': category_sneakers, 'price': '12', 'date_make': date.today().isoformat(),
             'date_update':  date.today().isoformat()},
            {'name': 'Adidas', 'category': category_sneakers, 'price': '14', 'date_make': date.today().isoformat(),
             'date_update': date.today().isoformat()},
            {'name': 'Nike', 'category': category_blouses, 'price': '20', 'date_make': date.today().isoformat(),
             'date_update': date.today().isoformat()},
            {'name': 'Adidas', 'category': category_blouses, 'price': '17', 'date_make': date.today().isoformat(),
             'date_update': date.today().isoformat()},
            {'name': 'Nike', 'category': category_pants, 'price': '21',
             'date_make': date.today().isoformat(),
             'date_update': date.today().isoformat()},
            {'name': 'Adidas', 'category': category_pants, 'price': '22',
             'date_make': date.today().isoformat(),
             'date_update': date.today().isoformat()},
            {'name': 'Nike', 'category': category_socks, 'price': '3',
             'date_make': date.today().isoformat(),
             'date_update': date.today().isoformat()},
            {'name': 'Adidas', 'category': category_socks, 'price': '2',
             'date_make': date.today().isoformat(),
             'date_update': date.today().isoformat()},
        ]

        for product_item in product_list:
            Sneakers.objects.create(**product_item)
