class Task:
    """Base task class."""

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self._completed = False

    @property
    def completed(self):
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
        self.deadline = deadline

    def is_overdue(self, current_date: str) -> bool:
        """Check if task is overdue."""
        return self.completed

    def __repr__(self) -> str:
        """Override to show deadline."""
        base = super().__repr__()
        return f"{base} (Due: {self.deadline})"
