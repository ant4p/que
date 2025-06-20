# Generated by Django 5.2.3 on 2025-06-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_status'),
        ('printers', '0002_printer_created_at_printer_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='printers',
            field=models.ManyToManyField(blank=True, null=True, to='printers.printer', verbose_name='Принтеры'),
        ),
    ]
