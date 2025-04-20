# task_management/urls.py

from django.urls import path
from .views import TaskCreateView, TaskAssignView, UserTasksView
from .auth_views import RegisterView, LoginView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('tasks/', TaskCreateView.as_view(), name='create-task'),
    path('tasks/assign/', TaskAssignView.as_view(), name='assign-task'),
    path('users/<int:user_id>/tasks/', UserTasksView.as_view(), name='user-tasks'),
]