from django.db import models
from django.urls import reverse

from core.models import BaseModel


class Printer(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Принтер")
    slug = models.SlugField(max_length=220, verbose_name="Slug")
    serial_number = models.CharField(max_length=300, verbose_name="Серийный номер")

    class Meta:
        db_table = "printers"
        verbose_name = "Принтер"
        verbose_name_plural = "Принтеры"
        ordering = ["-id"]

    def __str__(self):
        return str(self.title)

    def get_success_url(self):
        return reverse("printers:printer", kwargs={"slug": self.object.slug})

    def get_absolute_url(self):
        return reverse("printers:printer", kwargs={"slug": self.slug})
