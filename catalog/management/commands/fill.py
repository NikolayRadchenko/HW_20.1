from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Овощи'},
            {'name': 'Фрукты'},
            {'name': 'Крупы'},
        ]

        product_list = [
            {'name': 'Морковь', 'category': 'Овощи', 'price': '12', 'date_make': '18.07.2023',
             'date_update':  '18.07.2023'},
            {'name': 'Капуста', 'category': 'Овощи', 'price': '14', 'date_make': '18.07.2023',
             'date_update': '18.07.2023'},
            {'name': 'Ананас', 'category': 'Фрукты', 'price': '20', 'date_make': '18.07.2023',
             'date_update': '18.07.2023'},
            {'name': 'Апельсин', 'category': 'Фрукты', 'price': '17', 'date_make': '18.07.2023',
             'date_update': '18.07.2023'},
            {'name': 'Манка', 'category': 'Крупы', 'price': '2', 'date_make': '18.07.2023',
             'date_update': '18.07.2023'},
            {'name': 'Гречка', 'category': 'Крупы', 'price': '3', 'date_make': '18.07.2023',
             'date_update': '18.07.2023'},
        ]

        Category.objects.all().delete()
        Product.objects.all().delete()

        for category_item in category_list:
            Category.objects.create(**category_item)

        for product_item in product_list:
            Product.objects.create(**product_item)
