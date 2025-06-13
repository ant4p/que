from django.contrib import admin
from printers.models import Printer


class PrinterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Printer, PrinterAdmin)
