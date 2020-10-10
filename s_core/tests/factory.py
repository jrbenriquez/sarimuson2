import factory.django

from sarimuson.users.tests.factories import UserFactory

from ..models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    user = factory.SubFactory(UserFactory)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    mobile_number = factory.Faker("phone_number")
