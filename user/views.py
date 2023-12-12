from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):  # 회원정보 수정 전용인데 이거 나중에 커스텀 할거임. 우리 프로젝엔 필요없
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate a token for the newly registered user
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'user_id': user.id,
                'email': user.email,
                'token': token.key,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


CSRF_TRUSTED_ORIGINS = ["http://http://127.0.0.1:8000/user/login/"]


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Create or retrieve an authentication token for the user
            token, created = Token.objects.get_or_create(user=user)

            # Return the user data along with the token
            return Response({
                'user_id': user.id,
                'email': user.email,
                'token': token.key,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
