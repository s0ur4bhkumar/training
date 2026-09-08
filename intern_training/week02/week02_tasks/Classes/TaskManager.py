from Task import Task, UrgentTask


class TaskManager:
    """Manage a collection of tasks."""

    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the list."""

        self.tasks.append(task)

    def get_incomplete_tasks(self) -> list[Task]:
        """Return all incomplete tasks."""
        return list(filter(lambda x: not x.completed, self.tasks))

    def get_completed_tasks(self) -> list[Task]:
        """Return all completed tasks."""
        return list(filter(lambda x: x.completed, self.tasks))

    def mark_task_complete(self, title: str) -> bool:
        """Find task by title and mark complete. Return True if found."""
        for task in self.tasks:
            if task.title == title:
                _ = task.mark_complete
                return True
        return False

    def __len__(self) -> int:
        """Return number of tasks."""
        return len(self.tasks)


if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task(Task("Buy milk", "Get 2 liters"))
    manager.add_task(UrgentTask("Submit report", "Q4 report", "2024-12-31"))
    print(len(manager))  # 2
    print(manager.get_incomplete_tasks())
