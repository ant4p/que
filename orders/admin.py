from django.contrib import admin
from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "time_difference",
        "client",
        "printers__title",
        "get_printers",
        "status",
    )
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("time_difference",)

    @admin.display(description="Принтеры")
    def get_printers(self, obj):
        return "\n".join([str(p) for p in obj.printers.all()])


admin.site.register(Order, OrderAdmin)
