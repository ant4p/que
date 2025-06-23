from django.contrib import admin

from reports.models import Report


class ReportAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Report, ReportAdmin)
