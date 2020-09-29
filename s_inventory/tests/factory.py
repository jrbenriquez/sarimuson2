import factory.django

from ..models import Category
from ..models import Item


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("bs")
    description = factory.Faker("bs")


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    name = factory.Faker("bs")
    price = 1000
    category = factory.SubFactory(CategoryFactory)
