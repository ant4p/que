from django.db import models
from django.db.models import (
    F,
    Avg,
    DateField,
    DateTimeField,
    DurationField,
    ExpressionWrapper,
    Sum,
    Value,
    fields,
)
from django.db.models.functions import Cast, ExtractHour
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

    def get_instance(self):
        instance = Report.objects.get(slug=self.kwargs["slug"])
        return instance

    def get_orders(self):
        instanse = self.get_instance()
        orders = (
            Order.objects.filter(start_time__date__gte=str(instanse.start_day))
            .filter(end_time__date__lte=str(instanse.end_day))
            .filter(printers__in=instanse.printers.all())
        )
        return orders

    def add_time_diff_to_orders(self):
        orders = self.get_orders()
        orders = orders.annotate(
            new_field=ExpressionWrapper(
                F("end_time") - F("start_time"),
                output_field=DurationField(),
            )
        )
        return orders

    def add_total_summ(self):
        orders = self.add_time_diff_to_orders()
        total_sum = orders.aggregate(Sum("new_field"))["new_field__sum"]
        print(total_sum)
        return total_sum
    
    def add_orders_count(self):
        orders = self.get_orders()
        count = orders.count()
        return count

    def get_printers(self):
        printers = Printer.objects.filter(report__slug=self.kwargs["slug"])
        return printers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        printers = self.get_printers()
        context["printers_data"] = printers

        orders = self.add_time_diff_to_orders()
        context["orders_data"] = orders

        total_sum = self.add_total_summ()
        if total_sum is None:
            context["total_sum_data"] = "Данные отсутствуют"
        else:
            context["total_sum_data"] = total_sum

        orders_count = self.add_orders_count()
        context["orders_count"] = orders_count

        return context
