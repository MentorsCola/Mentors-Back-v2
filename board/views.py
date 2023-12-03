from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
from board.forms import BoardForm


def board_list(request):
    boards = Board.objects.all()
    return render(request, 'board/board_list.html', {'boards': boards})


def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'board/board_detail.html', {'board': board})


@login_required
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # 현재 로그인한 사용자를 글의 작성자로 지정
            board = form.save(commit=False)
            board.author = request.user
            board.save()
            return redirect('board_list')
    else:
        form = BoardForm()

    return render(request, 'board/board_form.html', {'form': form})


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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('board_list')  # 회원가입 후 이동할 페이지 지정
    else:
        form = UserCreationForm()

    return render(request, 'board/signup.html', {'form': form})