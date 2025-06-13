from django.urls import path

from printers.views import PrinterListView, PrinterView

app_name = 'printers'

urlpatterns = [
    path("", PrinterListView.as_view(), name='printers_list'),
    path('<slug:slug>/', PrinterView.as_view(), name='printer'),
]
