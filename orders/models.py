from datetime import datetime
from django.db import models
from django.urls import reverse

from core.models import BaseModel
from printers.models import Printer


class Order(BaseModel):
    STATUS_CHOICE = (
        ("create", "create"),
        ("process", "process"),
        ("complete", "complete"),
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
        default="create",
        null=True,
        blank=True,
        verbose_name="Статус",
    )
    printers = models.ManyToManyField(
        Printer, blank=True, null=True, verbose_name="Принтеры"
    )

    class Meta:
        db_table = "orders"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-id"]

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
