from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce

from s_inventory.models.item import QuantityUnit
from .mixins import TimeStampedMixin


class PurchaseItem(TimeStampedMixin):
    purchase = models.ForeignKey("s_core.Purchase", related_name="items", on_delete=models.PROTECT)
    item_stock = models.ForeignKey("s_inventory.ItemStock", related_name="purchases", on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_unit = models.ForeignKey("s_inventory.QuantityUnit", related_name="+", on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=11, decimal_places=2)

    def compute_total_price(self):
        if hasattr(self.quantity_unit, 'price'):
            price = self.quantity_unit.price.value
        else:
            price = self.item_stock.item.price

        return self.quantity * price

    def save(self, *args, **kwargs):
        self.amount = self.compute_total_price()
        super().save(*args, **kwargs)


class Purchase(TimeStampedMixin):
    class PurchaseStatusChoices(models.TextChoices):
        COMPLETE = "OK"
        SET_ASIDE = "SA"
        NEW = "NW"

    status = models.CharField(
        max_length=2,
        choices=PurchaseStatusChoices.choices,
        default=PurchaseStatusChoices.NEW,
    )
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    amount_received = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    change = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    customer = models.ForeignKey('s_core.Customer', related_name='purchases', on_delete=models.PROTECT)

    def signal_deduct_stock(self, stock, quantity):
        # TODO Make this a signal as stock deduction is a side effect due to creation of a Purchase Item
        if stock.quantity < quantity:
            raise Exception(
                f'Quantity being added is more than the available stock '
                f'quantity: {quantity} > {stock.quantity}'
            )
        stock.quantity -= Decimal(quantity)
        stock.save()

    def _update_purchase_amount(self):
        total_item_amount = self.items.aggregate(total=Coalesce(Sum('amount'), 0))['total']
        self.amount = total_item_amount
        self.save(update_fields=['amount'])

    def add_purchase_item(self, item_stock, quantity: Decimal, quantity_unit):
        if item_stock.quantity < quantity:
            raise Exception(
                f'Quantity being added is more than the available stock '
                f'quantity: {quantity} > {item_stock.quantity}'
            )
        purchase_item = PurchaseItem.objects.create(
            purchase=self,
            item_stock=item_stock,
            quantity=quantity,
            quantity_unit=quantity_unit
        )
        self.signal_deduct_stock(item_stock, quantity)
        self._update_purchase_amount()
        return purchase_item

    def money_received(self, amount: Decimal):
        if isinstance(self.amount, Decimal) and amount > self.amount:
            self.amount_received = amount
            self.change = amount - self.amount
            self.status = self.PurchaseStatusChoices.COMPLETE
            self.save()
            return self.change
        raise Exception(f'Received {amount} but purchase amount was {self.amount}. Received should be > Purchased')
