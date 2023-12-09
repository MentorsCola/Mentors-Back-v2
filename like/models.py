from django.db import models

from board.models import Board
from user.models import User


class Like(models.Model):
    user_email = models.ForeignKey(User, on_delete=models.CASCADE)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='liked_board_id')

    def __str__(self):
        return f'{self.user} likes {self.board}'
