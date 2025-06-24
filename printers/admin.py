from django.contrib import admin
from orders.models import Order
from printers.models import Printer


class PrinterAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "slug",
        "status",
        "serial_number",
        "get_printers_all",
        "created_at",
        "updated_at",
    ]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = (
        "get_printers",
        "created_at",
        "updated_at",
        "get_printers_all",
    )
    list_display = (
        "title",
        "get_printers",
        "status",
    )

    def save_model(self, request, obj, form, change):
        obj.save()
        return super().save_model(request, obj, form, change)

    @admin.display(description="Заказы")
    def get_printers(self, obj):
        orders = list(Order.objects.filter(printers__id=obj.id))
        return orders

    @admin.display(description="Заказы")
    def get_printers_all(self, obj):
        orders = Order.objects.filter(printers__id=obj.id).values_list(
            "title", flat=True
        )
        orders_list = [x for x in orders]
        print(orders_list)
        return ", ".join([x for x in orders_list])


admin.site.register(Printer, PrinterAdmin)
