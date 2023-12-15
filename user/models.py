import random

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


from nicknames.models import Nicknames


# 헬퍼 클래스
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)

        def clean(self):
            try:
                validate_email(self.email)
            except ValidationError as e:
                raise ValidationError({'email': 'Invalid email address'}) from e

        if self.filter(email=email).exists():
            raise ValueError('이미 등록된 이메일 주소입니다.')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여
        """
        superuser = self.create_user(
            email=email,
            password=password,
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True

        superuser.save(using=self._db)
        return superuser


# AbstractBaseUser를 상속해서 유저 커스텀
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    id_nickname = models.ForeignKey(Nicknames, on_delete=models.CASCADE, null=True, blank=True)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = 'email'

    def nickSave(self, *args, **kwargs):
        print(f"id_nickname before: {self.id_nickname}")

        if not self.id_nickname:
            all_nicknames = Nicknames.objects.all()
            if all_nicknames:
                random_nickname = random.choice(all_nicknames)
                self.id_nickname = random_nickname
                random_nickname.user_set.add(self)

        super().save(*args, **kwargs)
