from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'id_nickname']

    def create(self, validated_data):
        # 비밀번호를 암호화하여 저장
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user



