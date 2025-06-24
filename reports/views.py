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
        print(context)
        instanse = Report.objects.get(slug=self.kwargs["slug"])
        start_day = str(instanse.start_day)
        print("taatatat")
        print("taatatat")
        print("taatatat")
        print("taatatat")
        print(start_day)
        end_day = str(instanse.end_day)
        print(end_day)
        orders = (
            Order.objects.filter(start_time__date__gte=start_day)
            .filter(end_time__date__lte=end_day)
            # .filter(printers__slug=instanse.printers)
        )

        context["orders_data"] = orders
        printers = Printer.objects.filter(report__slug=self.kwargs["slug"])
        context["printers_data"] = printers
        return context
