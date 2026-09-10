from datetime import date, timedelta

from django.utils import timezone

from .models import Task  # Replace 'myapp' with your actual app name

today = date.today()

tasks_data = [
    Task(
        title="Set up CI/CD Pipeline",
        description="Configure GitHub Actions for automated testing and deployment.",
        status="In Progress",
        due_date=today + timedelta(days=2),
    ),
    Task(
        title="Design Landing Page",
        description="Create wireframes and high-fidelity mockups in Figma.",
        status="Todo",
        due_date=today + timedelta(days=5),
    ),
    Task(
        title="Fix Authentication Bug",
        description="Resolve JWT token expiration issue on page refresh.",
        status="In Progress",
        due_date=today + timedelta(days=1),
    ),
    Task(
        title="Database Optimization",
        description="Add indexes on frequently queried foreign key fields.",
        status="Todo",
        due_date=today + timedelta(days=7),
    ),
    Task(
        title="Write API Documentation",
        description="Document all REST endpoints using Swagger/OpenAPI.",
        status="Completed",
        due_date=today - timedelta(days=1),
    ),
    Task(
        title="Setup Redis Caching",
        description="Implement caching for expensive database queries.",
        status="Todo",
        due_date=today + timedelta(days=4),
    ),
    Task(
        title="User Interview Synthesis",
        description="Analyze feedback from recent user testing sessions.",
        status="In Progress",
        due_date=today + timedelta(days=3),
    ),
    Task(
        title="Unit Test Coverage",
        description="Increase unit test coverage for payment service to 85%.",
        status="Todo",
        due_date=today + timedelta(days=10),
    ),
    Task(
        title="Security Audit",
        description="Review dependency vulnerabilities and update outdated packages.",
        status="Completed",
        due_date=today - timedelta(days=3),
    ),
    Task(
        title="Prepare Release Notes",
        description="Draft release notes for version 2.1.0 release.",
        status="Todo",
        due_date=today + timedelta(days=6),
    ),
]

# Bulk insert all 10 tasks in a single query
Task.objects.bulk_create(tasks_data)
