from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Board


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)  # 필요한 필드만 포함

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # username과 관련된 필드 제거
        self.fields.pop('username')
        self.fields.pop('password2')


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']
