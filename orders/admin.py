from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Order, OrderAdmin)
