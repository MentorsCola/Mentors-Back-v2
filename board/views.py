from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import permissions
from rest_framework.views import APIView

from .models import Board
from board.forms import BoardForm


class BoardList(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        boards = Board.objects.all()
        board_data = []

        for board in boards:
            board_data.append({
                'id': board.id,
                'title': board.title,
                'nickname_author': board.nickname_author.nicknames if board.nickname_author else None,
                'dt_created': board.dt_created,
                'dt_modified': board.dt_modified
            })

        return JsonResponse({'boards': board_data})


class Board_detail(View):
def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'board/board_detail.html', {'board': board})


def board_edit(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            board.save()
            return redirect('board_detail', pk=board.pk)
    else:
        form = BoardForm(instance=board)
    return render(request, 'board/board_form.html', {'form': form})


def board_delete(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect('board_list')
