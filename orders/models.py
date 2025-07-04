from datetime import datetime
from django.db import models
from django.db.models import Q
from django.urls import reverse

from core.models import BaseModel
from printers.models import Printer


class Order(BaseModel):
    STATUS_CHOICE = (
        ("create", "Создан"),
        ("process", "В работе"),
        ("complete", "Выполнен"),
        ("correction", "Коррекция"),
        ("canceled", "Отменён"),
    )

    title = models.CharField(max_length=200, verbose_name="Заказ")
    slug = models.SlugField(max_length=220, verbose_name="Slug")
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name="Количество")
    material = models.CharField(max_length=200, verbose_name="Материал")
    client = models.CharField(max_length=200, verbose_name="Клиент")
    start_time = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Начало выполнения"
    )
    end_time = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Конец выполнения"
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICE,
        default="Создан",
        null=True,
        blank=True,
        verbose_name="Статус",
    )
    printers = models.ManyToManyField(Printer, blank=True, verbose_name="Принтеры")

    class Meta:
        unique_together = ('start_time', 'end_time')
        db_table = "orders"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-id"]

    def order_unique(self, model, start_time, end_time, **kwargs):
        query = Q(start_time__lte=end_time, end_time_gte=start_time)
        if kwargs:
            query &= Q(**kwargs)
        return model.objects.filter(query).exists()

    
    def save(self, *args, **kwargs):
        # date_time = Order.objects.filter(Q(start_time__lte=self.start_time) & Q(end_time__gte=self.end_time))
        # print(date_time)
        if Order.objects.filter(Q(start_time__lte=self.start_time) & Q(end_time__gte=self.end_time)):
             super().save(*args, **kwargs)
        else:
            print('NONONO')

    def __str__(self):
        return str(self.title)

    def get_success_url(self):
        return reverse("order", kwargs={"slug": self.object.slug})

    def get_absolute_url(self):
        return reverse("orders:order", kwargs={"slug": self.slug})

    @property
    def time_difference(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return None
