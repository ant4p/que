# Generated by Django 5.2.3 on 2025-06-24 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_printers_at_orders'),
        ('printers', '0006_remove_printer_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='printers_at_orders',
        ),
        migrations.AddField(
            model_name='order',
            name='printers',
            field=models.ManyToManyField(blank=True, to='printers.printer', verbose_name='Принтеры'),
        ),
    ]
