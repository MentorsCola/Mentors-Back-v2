from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from board.forms import BoardForm


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