import random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from nicknames.models import Nicknames


# 헬퍼 클래스
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)

        # Check if a user with the given email already exists
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
        # 회원가입 시 자동으로 랜덤 닉네임 할당
        if not self.id_nickname:
            all_nicknames = Nicknames.objects.all()
            if all_nicknames:
                random_nickname = random.choice(all_nicknames)
                self.id_nickname = random_nickname
                random_nickname.user_set.add(self)
            else:
                # 만약 닉네임이 하나도 없다면 기본 닉네임 또는 다른 로직을 적용하는데 그럴 일 없음
                default_nickname = Nicknames.objects.get(nicknames="내오늘안으로빚갚으리오")  # 예시로 id가 1인 닉네임을 사용
                self.id_nickname = default_nickname

        super(User, self).save(*args, **kwargs)


user_data = {
    "email": "test119@email.com",
    "password": "test11234"
}

try:
    new_user = User.objects.create_user(**user_data)
    new_user.nickSave()

    print({
        "id": new_user.id,
        "email": new_user.email,
        "password": new_user.password,
        "id_nickname": new_user.id_nickname.nicknames if new_user.id_nickname else None
    })
except ValueError as e:
    print(f"Error: {e}")