"""
Task class
"""

from datetime import date


class Task:
    """Base task class."""

    def __init__(self, title: str, description: str):
        self.title: str = title
        self.description: str = description
        self._completed: bool = False

    @property
    def completed(self):
        """
        getter method for complete attribute
        """
        return self._completed

    @completed.setter
    def mark_complete(self) -> None:
        """Mark task as completed."""
        self._completed = True

    def __repr__(self) -> str:
        status = "✓" if self.completed else "○"
        return f"{status} {self.title}"


class UrgentTask(Task):
    """Urgent task with deadline."""

    def __init__(self, title: str, description: str, deadline: str):
        super().__init__(title, description)
        self.deadline: str = deadline

    def is_overdue(self, current_date: str) -> bool:
        """Check if task is overdue."""
        return date(
            int(current_date.split("-")[0]),
            int(current_date.split("-")[1]),
            int(current_date.split("-")[2]),
        ) > date(
            int(self.deadline.split("-")[0]),
            int(self.deadline.split("-")[1]),
            int(self.deadline.split("-")[2]),
        )

    def __repr__(self) -> str:
        """Override to show deadline."""
        base = super().__repr__()
        return f"{base} (Due: {self.deadline})"
