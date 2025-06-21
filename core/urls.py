from django.urls import path

from core.views import ShowMainPage



app_name = "core"

urlpatterns = [
    path("", ShowMainPage.as_view(), name="main"),
]
