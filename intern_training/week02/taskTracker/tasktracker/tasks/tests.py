from django.test import TestCase

from .models import Task


class TasksListFilterTests(TestCase):
    def setUp(self):
        Task.objects.create(title="Buy groceries", description="Milk and bread", due_date="2026-09-12")
        Task.objects.create(title="Plan trip", description="Book hotel", due_date="2026-09-15")
        Task.objects.create(title="Write report", description="Draft summary", due_date="2026-09-12")

    def test_title_search_filters_tasks(self):
        response = self.client.get("/tasks_lists/", {"title": "trip"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Plan trip")
        self.assertNotContains(response, "Buy groceries")

    def test_due_date_filter_filters_tasks(self):
        response = self.client.get("/tasks_lists/", {"due_date": "2026-09-12"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Buy groceries")
        self.assertContains(response, "Write report")
        self.assertNotContains(response, "Plan trip")
