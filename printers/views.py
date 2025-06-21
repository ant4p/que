from django.views.generic import DetailView, ListView

from orders.models import Order
from printers.models import Printer


class PrinterListView(ListView):
    template_name = "printers/printers_main.html"
    context_object_name = "printers_list"

    def get_queryset(self):
        return Printer.objects.all()


class PrinterView(DetailView):
    model = Printer
    template_name = "printers/printer.html"
    context_object_name = "printer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders =  Order.objects.filter(printers__slug=self.kwargs['slug'])
        context['orders_data'] = orders
        return context
