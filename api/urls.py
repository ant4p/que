from rest_framework import routers

from api.views import OrderViewSet, PrinterViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('printers', PrinterViewSet)
router.register('orders', OrderViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
