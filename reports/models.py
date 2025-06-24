from datetime import datetime
from django.urls import reverse

from django.db import models

from core.models import BaseModel
from printers.models import Printer


class Report(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Название отчёта")
    slug = models.SlugField(max_length=110, verbose_name="Slug")
    start_day = models.DateField(
        default=datetime.now, blank=True, verbose_name="Начало отчета"
    )
    end_day = models.DateField(
        default=datetime.now, blank=True, verbose_name="Конец отчета"
    )
    printers = models.ManyToManyField(
        Printer, blank=True, null=True, verbose_name="Принтеры"
    )

    def get_absolute_url(self):
        return reverse("reports:report", kwargs={"slug": self.slug})

    class Meta:
        db_table = "reports"
        verbose_name = "Отчёт"
        verbose_name_plural = "Отчёты"
        ordering = ["-id"]

    def __str__(self):
        return str(self.title)
