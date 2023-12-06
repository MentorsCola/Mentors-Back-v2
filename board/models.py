from django.db import models
from django.contrib.auth.models import User

from MentorsBackV2 import settings
from user.models import Nickname


class Board(models.Model):  # 제목, 작성자, 내용, 작성일, 마지막 수정일
    title = models.CharField("제목", max_length=50, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField("내용", null=False)
    dt_created = models.DateTimeField("작성일", auto_now_add=True, null=False)
    dt_modified = models.DateTimeField("수정일", auto_now=True, null=False)
    # like = models.ForeignKey(Like, on_delete=models.CASCADE,)
    nickname_author = models.ForeignKey(Nickname, on_delete=models.CASCADE,)

    def __str__(self):
        return self.title
