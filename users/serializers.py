from rest_framework import serializers
from .models import UserSanay

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSanay
        fields = '__all__'