from django.urls import path

from orders.views import OrderView, OrdersListView

app_name = "orders"

urlpatterns = [
    path("", OrdersListView.as_view(), name="orders_list"),
    path("<slug:slug>/", OrderView.as_view(), name="order"),
]
