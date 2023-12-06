from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from board.models import Board
from like.models import Like


class LikeBoardView(View):
    def post(self, request, board_id):
        board = get_object_or_404(Board, pk=board_id)
        user = request.user

        # 사용자가 이미 해당 게시물에 대해 하트를 눌렀는지 확인
        like_exists = Like.objects.filter(user=user, board=board).exists()

        if like_exists:
            # 이미 누른 상태이면 하트 취소
            Like.objects.filter(user=user, board=board).delete()
            board.like -= 1
            board.save()
            message = '좋아요 취소'
        else:
            # 하트 누르기
            Like.objects.create(user=user, board=board)
            board.like += 1
            board.save()
            message = '좋아요'

        return JsonResponse({'message': message, 'like_count': board.like})