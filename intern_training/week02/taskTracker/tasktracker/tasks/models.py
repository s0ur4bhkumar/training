from datetime import datetime
from typing import override

from django.db import models


class Task(models.Model):
    class Meta:
        get_latest_by = "created_at"

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=100, default="Todo")
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @override
    def __str__(self):
        return str(self.title)
