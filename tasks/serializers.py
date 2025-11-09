from rest_framework import serializers
from .models import Task
from users.serializers import UserSerializer
from projects.serializers import ProjectSerializer
from users.models import UserSanay

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=UserSanay.objects.all(),
        many=True
    )

    class Meta:
        model = Task
        fields = "__all__"

