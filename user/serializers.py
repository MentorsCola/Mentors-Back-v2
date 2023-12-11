from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'id_nickname']

    def validate_email(self, value):
        if not value.strip():  # Ensure email is not empty or just whitespace
            raise serializers.ValidationError("Email cannot be empty.")
        return value
