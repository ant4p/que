# Generated by Django 5.2.3 on 2025-06-21 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0003_alter_printer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='printer',
            options={'ordering': ['-id'], 'verbose_name': 'Принтер', 'verbose_name_plural': 'Принтеры'},
        ),
    ]
