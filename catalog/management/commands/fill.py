from django.core.management import BaseCommand

from catalog.models import Product, Category


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

        category1 = Category.objects.get(name='Кроссовки')
        category2 = Category.objects.get(name='Одежда')

        product_list = [
            {'name': 'Nike', 'category': f'{category1}', 'price': '12', 'date_make': '18.07.2023',
             'date_update':  '18.07.2023'},
            {'name': 'Adidas', 'category': f'{category1}', 'price': '14', 'date_make': '18.07.2023',
             'date_update': '18.07.2023'},
            {'name': 'Майка Nike', 'category': f'{category2}', 'price': '20', 'date_make': '18.07.2023',
             'date_update': '18.07.2023'},
            {'name': 'Футболка Adidas', 'category': f'{category2}', 'price': '17', 'date_make': '18.07.2023',
             'date_update': '18.07.2023'},
        ]

        for product_item in product_list:
            Product.objects.create(**product_item)
