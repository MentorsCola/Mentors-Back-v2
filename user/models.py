import random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from nicknames.models import Nicknames


# 헬퍼 클래스
class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=email,
        )
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
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    id_nickname = models.ForeignKey(Nicknames, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = 'email'

    def nickSave(self, *args, **kwargs):
        # 회원가입 시 자동으로 랜덤 닉네임 할당
        if not self.id_nickname:
            all_nicknames = Nicknames.objects.all()
            if all_nicknames:
                random_nickname = random.choice(all_nicknames)
                self.id_nickname = random_nickname
                random_nickname.user_set.add(self)
            else:
                # 만약 닉네임이 하나도 없다면 기본 닉네임 또는 다른 로직을 적용
                default_nickname = Nicknames.objects.get(nicknames="내오늘안으로빚갚으리오")  # 예시로 id가 1인 닉네임을 사용
                self.id_nickname = default_nickname

                # 모델 필드의 기본값을 설정
                self._meta.get_field('id_nickname').default = self.id_nickname

            super().save(*args, **kwargs)