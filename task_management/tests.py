# task_management/tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Task

class TaskManagementAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create test users
        # self.user1 = User.objects.create_user(
        #     username='testuser1',
        #     email='testuser1@example.com',
        #     password='testpass123',
        #     first_name='Test',
        #     last_name='User1',
        #     mobile='1234567890'
        # )
        
        # self.user2 = User.objects.create_user(
        #     username='testuser2',
        #     email='testuser2@example.com',
        #     password='testpass123',
        #     first_name='Test',
        #     last_name='User2',
        #     mobile='9876543210'
        # )
        
        # Create a test task
        # self.task = Task.objects.create(
        #     name='Test Task',
        #     description='This is a test task',
        #     task_type='FEATURE'
        # )

    def test_create_task(self):
        """Test creating a new task"""
        url = reverse('create-task')
        data = {
            'name': 'New Task',
            'description': 'Description for the new task',
            'task_type': 'BUG'
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.get(id=2).name, 'New Task')

    def test_assign_task(self):
        """Test assigning a task to users"""
        url = reverse('assign-task')
        data = {
            'task_id': self.task.id,
            'user_ids': [self.user1.id, self.user2.id]
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that the task is assigned to both users
        self.task.refresh_from_db()
        self.assertEqual(self.task.assigned_users.count(), 2)
        self.assertTrue(self.user1 in self.task.assigned_users.all())
        self.assertTrue(self.user2 in self.task.assigned_users.all())

    def test_get_user_tasks(self):
        """Test getting tasks for a specific user"""
        # Assign the task to user1
        self.task.assigned_users.add(self.user1)
        
        url = reverse('user-tasks', kwargs={'user_id': self.user1.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.task.id)