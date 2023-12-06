from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'id_nickname']
        read_only_fields = ['id', 'email', 'password', 'id_nickname']
