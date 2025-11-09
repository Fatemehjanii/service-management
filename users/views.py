from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserSanay
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

class UserSanayList(APIView):
    def get(self, request):
        users = UserSanay.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserUpdate(APIView):
    def put(self, request, pk):
        user = get_object_or_404(UserSanay, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserDelete(APIView):
    def put(self, request, user_id):
        user = get_object_or_404(UserSanay, id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


