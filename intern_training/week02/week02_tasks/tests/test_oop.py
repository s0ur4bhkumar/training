import unittest
from datetime import date

from Classes.data_class import Task, UrgentTask
from Classes.TaskManager import TaskManager


class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Test", "Description")
        self.assertEqual(task.status, "todo")

    def test_empty_title_raises_error(self):
        with self.assertRaises(ValueError):
            Task("", "Description")

    def test_status_transition(self):
        task = Task("Test", "Desc")
        task.transition_to("in_progress")
        self.assertEqual(task.status, "in_progress")

    def test_invalid_transition_raises_error(self):
        task = Task("Test", "Desc")
        with self.assertRaises(ValueError):
            task.transition_to("done")  # Can't go from todo to done directly


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.task1 = Task("Task 1", "First task")
        self.task2 = Task("Task 2", "Second task")

    def test_add_task(self):
        self.manager.add_task(self.task1)
        self.assertEqual(len(self.manager), 1)

    def test_get_incomplete_task(self):
        self.manager.add_task(Task("Buy milk", "Get 2 liters", "done"))
        self.manager.add_task(UrgentTask("Submit report", "Q4 report", "todo"))
        self.assertEqual(len(self.manager.get_incomplete_tasks()), 1)

    def test_get_complete_task(self):
        self.manager.add_task(Task("Buy milk", "Get 2 liters", "done"))
        self.manager.add_task(UrgentTask("Submit report", "Q4 report", "done"))
        self.assertEqual(len(self.manager.get_completed_tasks()), 2)

    def test_mark_task_complete(self):
        self.manager.add_task(Task("Buy milk", "Get 2 liters", "done"))
        self.manager.add_task(UrgentTask("Submit report", "Q4 report", "todo"))
        self.assertEqual(self.manager.mark_task_complete(title="submit report"), False)


if __name__ == "__main__":
    _ = unittest.main()
