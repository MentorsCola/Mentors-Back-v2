from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'id_nickname']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        # 토큰 발행
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # 반환할 정보 구성
        response_data = {
            'email': user.email,
            'id_nickname': user.id_nickname,  # 이 부분은 필드에 따라서 적절한 방식으로 변경
            'token': access_token,
        }

        return response_data
)