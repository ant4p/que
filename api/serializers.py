from rest_framework import serializers

from orders.models import Order
from printers.models import Printer


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = [
            "id",
            "title",
            "slug",
            "serial_number",
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
