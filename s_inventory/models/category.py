from django.db import models
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey

__all__ = [
    "Category",
]


class Category(MPTTModel):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128, null=True, blank=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name
