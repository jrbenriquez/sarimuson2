from django.db import models

from .mixins import TimeStampedMixin


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
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    amount_received = models.DecimalField(max_digits=11, decimal_places=2)
    change = models.DecimalField(max_digits=11, decimal_places=2)


class PurchaseItem(TimeStampedMixin):
    purchase = models.ForeignKey("s_core.Purchase", related_name="items", on_delete=models.PROTECT)
    item = models.ForeignKey("s_inventory.Item", related_name="purchases", on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_unit = models.ForeignKey("s_inventory.QuantityUnit", related_name="+", on_delete=models.PROTECT)
