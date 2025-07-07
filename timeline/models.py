from django.db import models

from core.models import BaseModel

from printers.models import Printer



# Create your models here.
class Timeline(BaseModel):
    printer = models.OneToOneField(Printer, on_delete=models.CASCADE, verbose_name='Принтер')
    orders = models.ManyToManyField('orders.Order', blank=True, verbose_name="Заказы")

    class Meta:
        db_table = "timelines"
        verbose_name = "Время"

    def __str__(self):
        return str(self.printer)
