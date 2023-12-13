from django.urls import path

from user.views import UserListView, LoginAPIView, RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='user-register'),
    path('users/', UserListView.as_view(), name='user-list, user-signup'),
    path('login/', LoginAPIView.as_view(), name='user-login'),
]