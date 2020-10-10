from decimal import Decimal

from django.test import TestCase

from s_core.models import Purchase
from s_core.tests.factory import CustomerFactory
from s_inventory.models import QuantityUnit
from s_inventory.tests.factory import ItemFactory


class PurchaseTestCase(TestCase):

    def setUp(self):
        self.customer = CustomerFactory()
        self.item1 = ItemFactory()
        self.item2 = ItemFactory()
        self.item3 = ItemFactory()

        stock1 = self.item1.stocks.get()
        stock2 = self.item2.stocks.get()
        stock3 = self.item3.stocks.get()

        self.initial_quantity = 10
        stock1.quantity = self.initial_quantity
        stock2.quantity = self.initial_quantity
        stock3.quantity = self.initial_quantity

        stock1.save()
        stock2.save()
        stock3.save()

        self.quantity_unit = QuantityUnit.objects.last()

    def test_purchase(self):
        purchase = Purchase.objects.create(customer=self.customer)
        purchase_qs = Purchase.objects.filter(id=purchase.id)
        units_purchased = Decimal(10)
        purchase.add_purchase_item(self.item1.stocks.get(), units_purchased, self.quantity_unit)
        purchase.add_purchase_item(self.item2.stocks.get(), units_purchased, self.quantity_unit)
        purchase.add_purchase_item(self.item3.stocks.get(), units_purchased, self.quantity_unit)

        self.assertEqual(purchase.items.count(), 3)
        self.assertEqual(purchase.customer, self.customer)
        expected_price = Decimal(
            (self.item1.price * units_purchased)
            + (self.item2.price * units_purchased)
            + (self.item3.price * units_purchased)
        )
        self.assertEqual(purchase.amount, expected_price)
        self.assertEqual(
            self.item1.stocks.get().quantity,
            self.initial_quantity - units_purchased,
            'Item Stocks should be deducted the equivalent amount of Stocks Purchased'
        )
        self.assertEqual(purchase.status, Purchase.PurchaseStatusChoices.NEW)

        money_received = Decimal(50000)
        purchase.money_received(money_received)

        purchase = purchase_qs.get()
        self.assertEqual(purchase.amount_received, money_received)
        self.assertEqual(purchase.change, money_received - expected_price)
        self.assertEqual(purchase.status, Purchase.PurchaseStatusChoices.COMPLETE)
