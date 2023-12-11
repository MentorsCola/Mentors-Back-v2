from django.urls import path

from user.views import UserListView, UserDetailView, LoginAPIView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list, user-signup'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', LoginAPIView.as_view(), name='user-login'),
]