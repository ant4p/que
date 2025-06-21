from django.contrib import admin
from orders.models import Order
from printers.models import Printer


class PrinterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display =  (
        "title",
        "get_printers",
    )

    @admin.display(description="Заказы")
    def get_printers(self, obj):
        orders = Order.objects.filter(printers__id=obj.id, status='create')
        return list(orders)

admin.site.register(Printer, PrinterAdmin)
