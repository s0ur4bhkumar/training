from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = ["title", "status", "due_date", "created_at"]
    list_display = ["title", "status", "due_date", "created_at"]
    search_fields = ["title", "description"]
    list_filter = ["status", "due_date"]


admin.site.register(Task, TaskAdmin)
