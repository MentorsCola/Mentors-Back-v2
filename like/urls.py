from django.urls import path

from like.views import LikeBoardView

urlpatterns = [
    path('<int:board_id>/', LikeBoardView.as_view(), name='like-board'),
]