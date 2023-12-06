from rest_framework import generics
from nickname.models import Nickname


class NicknameView(generics.ListCreateAPIView):
    queryset = Nickname.objects.all()
