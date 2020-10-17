from django.db import models

DEFAULT_STOCK_NAME = "Default Stock"
DEFAULT_QUANTITY = ("pc", "Piece")


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
#        if not self.stocks.all():
#            try:
#                qty_unit = QuantityUnit.objects.get(short_name=DEFAULT_QUANTITY[0])
#            except QuantityUnit.DoesNotExist:
#                qty_unit = QuantityUnit.objects.create(name=DEFAULT_QUANTITY[1], short_name=DEFAULT_QUANTITY[0])
#            ItemStock.objects.create(item=self, description=DEFAULT_STOCK_NAME, quantity=1, quantity_unit=qty_unit)


class ItemStock(models.Model):
    item = models.ForeignKey("s_inventory.Item", related_name="stocks", on_delete=models.CASCADE)
    description = models.CharField(max_length=32, null=True, blank=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_unit = models.ForeignKey("s_inventory.QuantityUnit", related_name="+", on_delete=models.PROTECT)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)

    # Keeping this here as syntax reference for when we do simple checks to
    # fields that we track for changes
    # START SYNTAX

    __original_price_per_unit = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_price_per_unit = self.price_per_unit

    # END SYNTAX

    def __str__(self):
        return f"{self.item} - ({self.description})"

    def save(self, *args, **kwargs):
        # Set the quantity unit price to the item price if price_per_unit is not set
        if not self.price_per_unit:
            self.price_per_unit = self.item.price
        super().save(*args, **kwargs)


class QuantityUnit(models.Model):
    name = models.CharField(max_length=32, unique=True)
    short_name = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f"{self.short_name}"


class QuantityUnitPrice(models.Model):
    stock = models.OneToOneField('s_inventory.ItemStock', related_name='price', on_delete=models.CASCADE)
    quantity_unit = models.ForeignKey('s_inventory.QuantityUnit', related_name='+', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return f"{self.stock.item.name}-{self.value}"
