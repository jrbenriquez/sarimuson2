from django.contrib import admin

from .models.customer import Customer
from .models.purchase import Purchase
from .models.purchase import PurchaseItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass


@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    pass
