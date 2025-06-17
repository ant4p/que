from rest_framework import viewsets

from api.serializers import OrderSerializer, PrinterSerializer
from orders.models import Order
from printers.models import Printer


class PrinterViewSet(viewsets.ModelViewSet):
    serializer_class = PrinterSerializer
    queryset = Printer.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
