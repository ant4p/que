from django.views.generic import DetailView, ListView

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
