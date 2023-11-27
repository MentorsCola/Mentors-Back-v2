from django.db import models


class Board(models.Model):  # 제목, 작성자, 내용, 작성일, 마지막 수정일
    title = models.CharField("제목", max_length=50, null=False)
    author = models.ForeignKey("작성자", on_delete=models.CASCADE)  # User 탈퇴시 게시글 같이 지우기(CASCADE) 쓰는 기능은 아니지만 일단 넣음
    content = models.TextField("내용", null=False)
    dt_created = models.DateTimeField("작성일", auto_now_add=True, null=False)
    dt_modified = models.DateTimeField("수정일", auto_now_add=True, null=False)
    like = models.IntegerField("하트", default=0)

    def __str__(self):
        return 'author : {}, title : {}'.format(self.author, self.title, self.content)
