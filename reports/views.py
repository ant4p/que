from django.views.generic import DetailView, ListView

from orders.models import Order
from printers.models import Printer
from reports.models import Report


class ReportsListView(ListView):
    template_name = "reports/reports_main.html"
    context_object_name = "reports_list"

    def get_queryset(self):
        return Report.objects.all()


class ReportView(DetailView):
    model = Report
    template_name = "reports/report.html"
    context_object_name = "report"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instanse = Report.objects.get(slug=self.kwargs["slug"])

        printers = Printer.objects.filter(report__slug=self.kwargs["slug"])
        context["printers_data"] = printers

        orders = (
            Order.objects.filter(start_time__date__gte=str(instanse.start_day))
            .filter(end_time__date__lte=str(instanse.end_day))
            .filter(printers__in=instanse.printers.all())
        )
        context["orders_data"] = orders

        return context
