from datetime import datetime
from django.core.exceptions import ValidationError
from django.db import models

# from django.db.models import Q
from django.urls import reverse

from core.models import BaseModel
from timeline.models import Timeline


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
    printers = models.ManyToManyField(Timeline, blank=True, verbose_name="Принтеры")

    class Meta:
        unique_together = ("start_time", "end_time")
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
    
    def clean(self):
        super().clean()
        if self.end_time <= self.start_time:
            raise ValidationError('Время окончания выполнения заказа должно быть больше времени начала заказа')
        if self.end_time == self.start_time:
            raise ValidationError('Время окончания выполнения заказа не должно равняться времени начала заказа')
        
        overlapping_orders = Order.objects.filter(
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,

            
        ).exclude(pk=self.pk)
        if overlapping_orders.exists():
            raise ValidationError(f'В данное время принтер занят заказом { overlapping_orders }')
        # return 
    
    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

    @property
    def time_difference(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return None
