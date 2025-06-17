from dataclasses import fields
from django.contrib import admin
from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = (
        'time_difference',
    )

admin.site.register(Order, OrderAdmin)
