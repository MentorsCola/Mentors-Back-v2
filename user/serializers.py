from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'id_nickname']

    def create(self, validated_data):
        # User 객체 생성
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        # 토큰 발행
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # 항상 id_nickname 값이 있는 경우 반환
        return {
            'email': user.email,
            'id_nickname': user.id_nickname,
            'token': access_token,
        }