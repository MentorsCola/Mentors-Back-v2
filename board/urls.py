from django.urls import path
from .views import board_list, board_detail, board_edit, board_delete

urlpatterns = [
    path('', board_list, name='board_list'),

    path('<int:pk>/', board_detail, name='board_detail'),
    path('<int:pk>/edit/', board_edit, name='board_edit'),
    path('<int:pk>/delete/', board_delete, name='board_delete'),


]
