from django.db import models

from board.models import Board
from user.models import User


class Like(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} likes {self.board}'
