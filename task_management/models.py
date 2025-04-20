# task_management/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Extended User model with additional fields required for the application.
    """
    mobile = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.username

class TaskType(models.TextChoices):
    """Enum for task types"""
    FEATURE = 'FEATURE', 'Feature'
    BUG = 'BUG', 'Bug'
    SUPPORT = 'SUPPORT', 'Support'
    ENHANCEMENT = 'ENHANCEMENT', 'Enhancement'

class TaskStatus(models.TextChoices):
    """Enum for task statuses"""
    PENDING = 'PENDING', 'Pending'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    COMPLETED = 'COMPLETED', 'Completed'
    CANCELLED = 'CANCELLED', 'Cancelled'

class Task(models.Model):
    """
    Task model to represent tasks in the system.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(
        max_length=20,
        choices=TaskType.choices,
        default=TaskType.FEATURE
    )
    completed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING
    )
    assigned_users = models.ManyToManyField(User, related_name='tasks', blank=True)
    
    def __str__(self):
        return self.name