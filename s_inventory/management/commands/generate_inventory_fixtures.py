import random

from django.db import transaction
from django.core.management.base import BaseCommand, CommandError
from s_inventory.models import Category
from s_inventory.models import QuantityUnit
from s_inventory.tests.factory import CategoryFactory
from s_inventory.tests.factory import ItemFactory
from s_inventory.tests.factory import ItemStockFactory
from s_inventory.tests.factory import QuantityUnitFactory

# TODO Create demo superuser


class Command(BaseCommand):
    help = 'Generates fixtures for loading sample data to work on'

    @transaction.atomic
    def handle(self, *args, **kwargs):

        SAMPLE_CATEGORIES = ["Drinks", "Candies", "Seasoning", "School Supplies"]

        SAMPLE_QUANTITY_UNITS = [
            ("Piece", "pc"),
            ("Kilo", "kilo"),
            ("Box", "box"),
            ("Set", "set"),
        ]
        self.stdout.write("Creating Categories", ending='')
        categories = []
        for category in SAMPLE_CATEGORIES:
            categories.append(CategoryFactory(name=category))

        self.stdout.write("Creating Quantity Units", ending='')
        quantity_units = []
        for name, short_name in SAMPLE_QUANTITY_UNITS:
            quantity_units.append(QuantityUnitFactory(name=name, short_name=short_name))

        number_of_items = random.randint(50, 200)

        self.stdout.write("Creating Items", ending='')
        for item_count in range(0, number_of_items):
            item = ItemFactory()
            for _ in range(0, random.randint(1, 10)):
                ItemStockFactory(
                    item=item,
                    quantity_unit=random.choice(quantity_units)
                )
