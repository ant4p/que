from datetime import datetime
from django.db import models
from django.urls import reverse


class Order(models.Model):

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
    # full_time = models.TimeField(editable=False, blank=True, verbose_name='Общее время')

    class Meta:
        db_table = "orders"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-id"]

    def __str__(self):
        return str(self.title)

    def get_success_url(self):
        return reverse("order", kwargs={"slug": self.object.slug})

    @property
    def time_difference(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return None
