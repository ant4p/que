from django.contrib import admin
from orders.models import Order
from printers.models import Printer


class PrinterAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "slug",
        "serial_number",
        "get_printers",
        "created_at",
        "updated_at",
    ]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = (
        "get_printers",
        "created_at",
        "updated_at",
    )
    list_display = (
        "title",
        "get_printers",
    )

    def save_model(self, request, obj, form, change):
        obj.save()
        return super().save_model(request, obj, form, change)

    @admin.display(description="Заказы")
    def get_printers(self, obj):
        orders = list(Order.objects.filter(printers__id=obj.id, status="create"))
        return orders


admin.site.register(Printer, PrinterAdmin)
