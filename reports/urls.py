from django.urls import path

from reports.views import ReportView, ReportsListView

app_name = "reports"

urlpatterns = [
    path("", ReportsListView.as_view(), name="reports_list"),
    path("<slug:slug>/", ReportView.as_view(), name="report"),
]
