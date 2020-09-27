from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    category = models.ForeignKey(
        "s_inventory.Category",
        related_name="items",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class ItemStock(models.Model):
    item = models.ForeignKey("s_inventory.Item", related_name="stocks", on_delete=models.CASCADE)
    description = models.CharField(max_length=32, null=True, blank=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_unit = models.ForeignKey("s_inventory.QuantityUnit", related_name="+", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.item} - ({self.description})"


class QuantityUnit(models.Model):
    name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.short_name}"
