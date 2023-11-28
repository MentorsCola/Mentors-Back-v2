from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('board/<int:pk>/', views.board_detail, name='board_detail'),
    path('board/new/', views.board_create, name='board_create'),
    path('board/<int:pk>/edit/', views.board_edit, name='board_edit'),
    path('board/<int:pk>/delete/', views.board_delete, name='board_delete'),
]
