from django.contrib import admin

from timeline.models import Timeline


class TimelineAdmin(admin.ModelAdmin):
    list_display = ['printer',]

admin.site.register(Timeline, TimelineAdmin)
