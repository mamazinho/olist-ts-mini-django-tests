from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):

    products = [
        {'name': 'Brinquedo', 'description': 'Brinquedos para crianças', 'price': 50.00},
        {'name': 'Caneta', 'description': 'Escritório', 'price': 2.50},
        {'name': 'Remédio', 'description': 'Remedão', 'price': 50},
    ]

    def handle(self, *args, **options):
        to_create = []

        for product in self.products:
            gr = Product(**product)
            to_create.append(gr)

        Product.objects.bulk_create(to_create, ignore_conflicts=True)