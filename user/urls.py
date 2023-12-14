from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserListView, LoginAPIView, RegisterAPIView, Logout

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='user-register'),
    path('users/', UserListView.as_view(), name='user-list, user-signup'),
    path('login/', LoginAPIView.as_view(), name='user-login'),
    path('logout/', Logout.as_view(), name='user-logout'),
    path('auth/refresh/', TokenRefreshView.as_view()), # jwt 토큰 재발급
]