from django.db import models

from nicknames.models import Nicknames
from user.models import User


class Board(models.Model):  # 제목, 작성자, 내용, 작성일, 마지막 수정일
    title = models.CharField("제목", max_length=50, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField("내용", null=False)
    dt_created = models.DateTimeField("작성일", auto_now_add=True, null=False)
    dt_modified = models.DateTimeField("수정일", auto_now=True, null=False)
    nickname_author = models.ForeignKey(Nicknames, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()
