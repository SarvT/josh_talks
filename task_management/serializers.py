# task_management/serializers.py

from rest_framework import serializers
from .models import User, Task

# task_management/serializers.py (update the UserSerializer)

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model
    """
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'mobile']

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model without nested user details
    """
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 
                  'completed_at', 'status', 'assigned_users']

class TaskDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model with nested user details
    """
    assigned_users = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 
                  'completed_at', 'status', 'assigned_users']

class TaskAssignmentSerializer(serializers.Serializer):
    """
    Serializer for task assignment endpoint
    """
    task_id = serializers.IntegerField()
    user_ids = serializers.ListField(
        child=serializers.IntegerField()
    )