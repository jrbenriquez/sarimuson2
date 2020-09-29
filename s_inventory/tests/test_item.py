from django.test import TestCase  # NOQA

from s_inventory.models import Category
from s_inventory.models import Item
from s_inventory.tests.factory import CategoryFactory
from s_inventory.tests.factory import ItemFactory


class ItemTest(TestCase):
    def setUp(self):
        self.item = ItemFactory()

    def test_create_item(self):
        self.assertIsInstance(self.item, Item)
        self.assertIsNotNone(self.item.name)
        self.assertIsNotNone(self.item.category)
        self.assertIsNotNone(self.item.price)
        self.assertEqual(self.item.stocks.all().count(), 1)

    def test_create_category(self):
        new_category = CategoryFactory()
        self.assertIsInstance(new_category, Category)
        self.assertIsNotNone(new_category.name)
        self.assertIsNotNone(new_category.description)
