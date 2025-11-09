from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from users.models import UserSanay
from .import serializers
from .import models
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from tasks.models import Task
from projects.models import Project
from django.utils import timezone
# Create your views here.
class TaskList(APIView):
    def get(self, request):
        obj = models.Task.objects.all()
        s = serializers.TaskSerializer(obj, many=True)
        return Response(s.data)

class TaskUpdate(APIView):
    def put(self, request, task_id):
        task = models.Task.objects.get(id=task_id)
        s = serializers.TaskSerializer(task, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=400)

class TaskDelete(APIView):
    def delete(self, request, task_id):
        task = models.Task.objects.get(id=task_id)
        task.delete()
        return Response(status=204)

class AssignTaskToProject(APIView):
    def put(self, request):
        task_id = request.data.get("task_id")
        project_id = request.data.get("project_id")

        task = get_object_or_404(Task, id=task_id)
        project = get_object_or_404(Project, id=project_id)

        # assign
        task.project = project
        task.save()

        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)




class UserTasks(APIView):
    def get(self, request, user_id):
        try:
            user = UserSanay.objects.get(id=user_id)
        except UserSanay.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        tasks = Task.objects.filter(assigned_to=user).order_by("start_time")
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskListByStartTime(generics.ListAPIView):
    queryset = Task.objects.all().order_by("start_time")
    serializer_class = TaskSerializer



class ProjectCreateAPIView(APIView):
    def post(self, request):
        name = request.data.get('name')
        owner_id = request.data.get('owner')

        if not name or not owner_id:
            return Response({"error": "Name and owner_id required"}, status=400)


        try:
            owner = UserSanay.objects.get(id=owner_id)
        except UserSanay.DoesNotExist:
            return Response({"error": "User not found"}, status=402)


        project, created = Project.objects.get_or_create(
            name=name,
            defaults={
                "description": "",
                "category": "web_development",
                "start_date": timezone.now(),
                "owner": owner
            }
        )


        return Response({"id": project.id, "name": project.name}, status=200)

class TaskCreateAPIView(APIView):
    def post(self, request):
        title = request.data.get('title')
        project_id = request.data.get('project')  # ID پروژه
        assigned_to_ids = request.data.get('assigned_to', [])  # لیست ID کاربران

        if not title or not project_id:
            return Response({"error": "Title and project_id required"}, status=400)

        # بررسی وجود پروژه
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=402)

        # بررسی وجود کاربران
        users = []
        for user_id in assigned_to_ids:
            try:
                user = UserSanay.objects.get(id=user_id)
                users.append(user)
            except UserSanay.DoesNotExist:
                return Response({"error": f"User {user_id} not found"}, status=402)

        # ایجاد Task با زمان خودکار
        task, created = Task.objects.get_or_create(
            title=title,
            project=project,
            defaults={
                "start_time": timezone.now(),
                "end_time": timezone.now()
            }
        )

        # اضافه کردن کاربران
        task.assigned_to.set(users)

        return Response({
            "id": task.id,
            "title": task.title,
            "project": project.id,
            "assigned_to": [u.id for u in users],
            "start_time": task.start_time,
            "end_time": task.end_time
        }, status=200)

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserSanay

class UserCreateAPIView(APIView):
    def post(self, request):
        full_name = request.data.get('full_name')

        if not full_name:
            return Response({"error": "full_name required"}, status=400)


        user, created = UserSanay.objects.get_or_create(
            full_name=full_name,
            defaults={
                "email": f"{full_name.replace(' ', '').lower()}@gmail.com",
                "role": "developer",
                "experience_years": 0,
                "skills": "",
                "join_date": timezone.now().date(),
                "is_active": True
            }
        )

        return Response({
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email
        }, status=200)

class AssignUsersToTaskAPIView(APIView):
    def put(self, request, task_id):
        assigned_to_ids = request.data.get('assigned_to', [])

        # بررسی وجود تسک
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=402)

        # بررسی وجود کاربران
        users = []
        for user_id in assigned_to_ids:
            try:
                user = UserSanay.objects.get(id=user_id)
                users.append(user)
            except UserSanay.DoesNotExist:
                return Response({"error": f"User {user_id} not found"}, status=402)

        # جایگزینی کل لیست کاربران Assigned
        task.assigned_to.set(users)

        return Response({
            "task_id": task.id,
            "assigned_to": [u.id for u in users]
        }, status=200)