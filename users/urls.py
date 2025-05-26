from django.urls import path

from users.apps import UsersConfig
from users.views import (CustomLoginView, CustomLogoutView, RegisterView,
                         UserDetailVew, UserUpdateView)

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('user_detail/<int:pk>/', UserDetailVew.as_view(), name='user_detail'),
    path('edit/<int:pk>/', UserUpdateView.as_view(), name='user_edit'),
]
