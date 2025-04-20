# task_management/views.py

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User, Task
from .serializers import TaskSerializer, TaskDetailSerializer, TaskAssignmentSerializer

class TaskCreateView(generics.CreateAPIView):
    """
    API endpoint to create a new task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAssignView(APIView):
    """
    API endpoint to assign a task to one or more users
    """
    def post(self, request):
        serializer = TaskAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            task_id = serializer.validated_data['task_id']
            user_ids = serializer.validated_data['user_ids']
            
            # Get the task
            task = get_object_or_404(Task, id=task_id)
            
            # Add users to the task
            for user_id in user_ids:
                user = get_object_or_404(User, id=user_id)
                task.assigned_users.add(user)
            
            task_serializer = TaskDetailSerializer(task)
            return Response(task_serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserTasksView(generics.ListAPIView):
    """
    API endpoint to get all tasks for a specific user
    """
    serializer_class = TaskDetailSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        return user.tasks.all()