from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import get_object_or_404
from tasks.models import Task
from users.models import UserSanay




class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class ProjectUpdate(APIView):
    def put(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDelete(APIView):
    def delete(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


