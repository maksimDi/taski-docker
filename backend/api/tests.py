from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Task


class TaskModelTest(TestCase):
    """Тесты для модели Task."""
    
    def test_create_task(self):
        """Тест создания задачи."""
        task = Task.objects.create(
            title='Test task',
            description='Test description'
        )
        self.assertEqual(task.title, 'Test task')
        self.assertEqual(task.description, 'Test description')


class TaskAPITest(TestCase):
    """Тесты для API задач."""
    
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
    
    def test_get_tasks(self):
        """Тест получения списка задач."""
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

