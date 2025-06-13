from django.views.generic import DetailView, ListView

from orders.models import Order


# Create your views here.
class OrdersListView(ListView):
    template_name = "orders/orders_main.html"
    context_object_name = "orders_list"

    def get_queryset(self):
        return Order.objects.all()


class OrderView(DetailView):
    model = Order
    template_name = "orders/order.html"
    context_object_name = "order"
