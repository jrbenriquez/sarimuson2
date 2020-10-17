import random
import factory.django

from ..models import Category
from ..models import Item
from ..models import ItemStock
from ..models import QuantityUnit


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("bs")
    description = factory.Faker("bs")


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    name = factory.Faker("bs")
    price = factory.LazyAttribute(lambda x: random.randint(50, 200))
    category = factory.SubFactory(CategoryFactory)


class QuantityUnitFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = QuantityUnit

    name = factory.Faker("bs")
    short_name = factory.Faker("bs")


class ItemStockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ItemStock

    item = factory.SubFactory(ItemFactory)
    description = factory.Faker('bs')
    quantity = factory.LazyAttribute(lambda x: random.randint(1, 100))
    quantity_unit = factory.SubFactory(QuantityUnitFactory)
    price_per_unit = factory.LazyAttribute(lambda x: random.randint(1, 150))
