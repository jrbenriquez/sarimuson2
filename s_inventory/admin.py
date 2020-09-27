from django.contrib import admin
from django.forms.models import BaseInlineFormSet

from s_inventory.models import Category
from s_inventory.models import Item
from s_inventory.models import ItemStock
from s_inventory.models import QuantityUnit


class ItemStockInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        kwargs["initial"] = [
            {
                "description": "Default Stock",
                "quantity": 1,
            }
        ]
        super().__init__(*args, **kwargs)


class ItemStockInline(admin.TabularInline):

    model = ItemStock
    extra = 0
    min_num = 1
    formset = ItemStockInlineFormSet


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "parent"]
    search_fields = [
        "name",
    ]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [
        ItemStockInline,
    ]
    list_display = ["name", "price"]


@admin.register(ItemStock)
class ItemStockAdmin(admin.ModelAdmin):
    list_display = [
        "item",
    ]


@admin.register(QuantityUnit)
class QuantityUnitAdmin(admin.ModelAdmin):
    list_display = ["short_name", "name"]
